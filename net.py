'''网络'''
import requests
import bs4
import tqdm

import loader
import utils

URL_PRE = "http://"+loader.SCHOOL+".pocketuni.net"
URL_TP = URL_PRE+"/index.php?app=event&mod=School&act=rank&k={type}&p={page}"
URL_USER = URL_PRE+"/index.php?app=home&mod=Account&act=index"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Connection": "close",
    "Cookie": loader.COOKIE
}


def get_res(url: str):
    '''从url获取一个Response'''
    try:
        return requests.get(url, headers=HEADERS, timeout=5)
    except:
        tqdm.tqdm.write("超时重试")
        return get_res(url)


def get_bs_instance(url: str):
    '''从url获取一个BeautifulSoup的实例'''
    return bs4.BeautifulSoup(get_res(url).content, "lxml")


def get_username():
    '''从个人信息页获取用户昵称'''
    return get_bs_instance(URL_USER).find(attrs={"name": "nickname"})["value"]


def get_rank_and_pages(type_: int):
    '''获取当前排名和总页数'''
    first_page = get_bs_instance(URL_TP.format(type=type_, page='1'))
    rank = utils.get_num(first_page.find(class_="myrank").string)
    # nodes = [i for i in first_page.find(class_="page plist").children]
    nodes = list(first_page.find(class_="page plist").children)
    pagecnt = int(nodes[6].string[2:])
    return rank, pagecnt
