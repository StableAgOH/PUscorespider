'''网络'''
import requests
import requests.adapters
import bs4

from instances import workbook
from loader import SCHOOL,COOKIE
from utils import get_num

URL_PRE = "http://"+SCHOOL+".pocketuni.net"
URL_TP = URL_PRE+"/index.php?app=event&mod=School&act=rank&k={type}"
URL_USER = URL_PRE+"/index.php?app=home&mod=Account&act=index"

HEADERS = {
    "Accept": "text/html",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Connection": "close",
    "Cookie": COOKIE
}


def get_res(url: str):
    '''从url获取一个Response'''
    ses = requests.session()
    ses.mount("http://", requests.adapters.HTTPAdapter(max_retries=3))
    return ses.get(url, headers=HEADERS, timeout=5)


def get_bs_instance(url: str):
    '''从url获取一个BeautifulSoup的实例'''
    return bs4.BeautifulSoup(get_res(url).content, "lxml")


def get_username():
    '''从个人信息页获取用户昵称'''
    return get_bs_instance(URL_USER).find(attrs={"name": "nickname"})["value"]


def get_rank_and_pages(type_: int):
    '''获取当前排名和总页数'''
    first_page = get_bs_instance(add_page(URL_TP.format(type=type_), 1))
    rank = get_num(first_page.find(class_="myrank").string)
    nodes = list(first_page.find(class_="page plist").children)
    pagecnt = int(nodes[6].string[2:])
    return rank, pagecnt


def add_page(url: str, page: int):
    '''给一个排行榜URL增加页码'''
    return url+"&p="+str(page)


def write_range(url_pre, begin: int, end: int):
    '''获取页码区间的数据并写入workbook'''
    for page in range(begin, end):
        table = get_bs_instance(add_page(url_pre, page)).table
        data_page = [
            [
                table.contents[stu].contents[attr].string
                for attr in range(1, 8, 2)
            ]
            for stu in range(3, len(table.contents), 2)
        ]
        workbook.write_data(data_page)
