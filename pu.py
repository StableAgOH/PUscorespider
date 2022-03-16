import json
import logging
import re
from pathlib import Path

import requests
import seaborn as sns
import tqdm
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from requests.adapters import HTTPAdapter

from book import MyBook

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

path_config = Path("config.json")
if path_config.exists():
    CONFIG = json.load(open(path_config, "r"))
else:
    CONFIG = {
        "cookie": input("请输入Cookie："),
        "school": input("请输入学校：")
    }
    json.dump(CONFIG, open(path_config, "w"), sort_keys=True, indent=4)

ENDPOINT = f"https://{CONFIG['school']}.pocketuni.net/index.php?app=event&mod=School&act=rank"

HEADERS = {
    "Accept": "text/html",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/87.0.4280.88 Safari/537.36",
    "Connection": "close",
    "Cookie": CONFIG['cookie']
}

TYPES = ("月度排名", "学期排名", "学年排名")


def get_bs(url: str):
    ses = requests.session()
    ses.mount("https://", requests.adapters.HTTPAdapter(max_retries=3))
    return BeautifulSoup(ses.get(url, headers=HEADERS, timeout=30).content, "lxml")


def input_yn(info: str):
    opt = input(info).upper()
    while opt not in ('Y', 'N'):
        logger.error("选项错误")
        opt = input(info).upper()
    return opt


if __name__ == "__main__":
    workbook = MyBook()
    if not workbook.exists() or input_yn("数据已存在，是否继续获取(Y/N)"):
        for i in range(1, 4):
            print(f"{i}. {TYPES[i - 1]}")

        tp = input("要爬取哪个类型的排名(1~3)：")
        while not tp.isdigit() or not 1 <= int(tp) <= 3:
            logger.error("类型错误")
            tp = input("要爬取哪个类型的排名(1~3)：")
        tp = int(tp) - 1

        workbook.write_title(TYPES[tp])
        first_page = get_bs(f"{ENDPOINT}&k={tp}&p=1")
        try:
            rank = int(re.match(r"\d+", first_page.find(class_="myrank").string).group())
            logger.info(f"当前排名为：{rank}")
        except AttributeError:
            logger.warning("无法获取当前排名")

        pagecnt = int(list(first_page.find(class_="page plist").children)[6].string[2:])
        pages = input(f"共有{pagecnt}页数据，要爬取几页数据(每页10个同学，0为爬取所有页)：")
        while not pages.isdigit() or not 0 <= int(pages) <= pagecnt:
            logger.error("页数错误")
            pages = input(f"共有{pagecnt}页数据，要爬取几页数据(每页10个同学，0为爬取所有页)：")
        pages = pagecnt if pages == '0' else int(pages)

        for page in tqdm.trange(1, pages + 1, ascii=True):
            table = get_bs(f"{ENDPOINT}&k={tp}&p={page}").table
            data_page = [
                [
                    table.contents[stu].contents[attr].string
                    for attr in range(1, 8, 2)
                ]
                for stu in range(3, len(table.contents), 2)
            ]
            workbook.write_data(data_page)
        workbook.save()
    else:
        workbook.load_data()

    if input_yn("是否进行数据分析(Y/N)") == 'Y':
        sns.histplot(workbook.scores, binwidth=4, kde=True)
        plt.title(f"{CONFIG['school']} PU Score")
        plt.xlabel("Score")
        plt.ylabel("Number of students")
        plt.show()
    logger.info("任务完成啦！ヽ(￣▽￣)ﾉ")
