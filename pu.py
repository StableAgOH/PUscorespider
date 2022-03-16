import json
import logging
import re
from pathlib import Path

import requests
import seaborn as sns
import tqdm
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

from book import MyBook

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

path_config = Path("config.json")
if path_config.exists():
    CONFIG = json.load(open(path_config, "r"))
else:
    CONFIG = {
        "mobile": input("请输入手机号："),
        "password": input("请输入密码："),
        "school": input("请输入学校：")
    }
    json.dump(CONFIG, open(path_config, "w"), sort_keys=True, indent=4)

URL_LOGIN = "https://pocketuni.net/index.php?app=home&mod=Public&act=doMobileLogin"
URL_RANK = f"https://{CONFIG['school']}.pocketuni.net/index.php?app=event&mod=School&act=rank"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/87.0.4280.88 Safari/537.36"
}
SESSION = requests.session()

TYPES = ("月度排名", "学期排名", "学年排名")


def get_bs(url: str):
    return BeautifulSoup(SESSION.get(url, headers=HEADERS, timeout=30).content, "lxml")


def input_yes(info: str):
    opt = input(info).upper()
    while opt not in ('Y', 'N'):
        logger.error("选项错误")
        opt = input(info).upper()
    return opt == 'Y'


if __name__ == "__main__":
    logger.info("尝试登录")
    res = SESSION.post(URL_LOGIN, {
        "mobile": CONFIG["mobile"],
        "password": CONFIG["password"]
    }, headers={
        **HEADERS,
        "X-Requested-With": "XMLHttpRequest"
    })
    if res.ok:
        logger.info("登录成功")
    else:
        logger.error("登陆失败")
        exit(0)

    workbook = MyBook()
    if not workbook.exists() or input_yes("数据已存在，是否继续获取(Y/N)"):
        for i in range(1, 4):
            print(f"{i}. {TYPES[i - 1]}")

        tp = input("要爬取哪个类型的排名(1~3)：")
        while not tp.isdigit() or not 1 <= int(tp) <= 3:
            logger.error("类型错误")
            tp = input("要爬取哪个类型的排名(1~3)：")
        tp = int(tp) - 1

        workbook.write_title(TYPES[tp])
        first_page = get_bs(f"{URL_RANK}&k={tp}&p=1")
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
            table = get_bs(f"{URL_RANK}&k={tp}&p={page}").table
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

    if input_yes("是否进行数据分析(Y/N)"):
        sns.histplot(workbook.scores, binwidth=4, kde=True)
        plt.title(f"{CONFIG['school']} PU Score")
        plt.xlabel("Score")
        plt.ylabel("Number of students")
        plt.show()
    logger.info("任务完成啦！ヽ(￣▽￣)ﾉ")
