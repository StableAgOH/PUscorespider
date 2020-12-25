'''工具函数'''
import os
import re
import requests
import bs4

import book
import constants as ct


def init_bs(url: str):
    '''从url获取一个BeautifulSoup的实例'''
    return bs4.BeautifulSoup(get_rq(url).content, "lxml")


def get_rq(url: str):
    '''从url获取一个get的requests'''
    return requests.get(url, headers=ct.HEADERS)


def get_num(string: bs4.NavigableString):
    '''使用正则表达式获得一个NavigableString中的数字'''
    return int(re.sub(r'\D', "", string))


def get_rank_and_pages(type_: int):
    '''获取当前排名和总页数'''
    first_page = init_bs(ct.URL_TP.format(type=type_, page='1'))
    rank = get_num(first_page.find(class_="myrank").string)
    nodes = []
    for i in first_page.find(class_="page plist").children:
        nodes.append(i)
    pagecnt = int(nodes[6].string[2:])
    return rank, pagecnt


def get_yn(info: str):
    '''获取用户输入的Y或N'''
    opt = input(info).upper()
    while opt not in ('Y', 'N'):
        opt = input(ct.ERR_OPT).upper()
    return opt


def whether_continue():
    '''是否需要继续爬取'''
    if os.path.exists(book.BOOK_PATH):
        opt = get_yn(ct.QST_CTN)
        if opt == 'Y':
            return True
        return False
    return True


def divide_int(pages: int):
    '''将页数按线程数均分'''
    blocks = pages // ct.THREAD_NUM
    remaind = pages % ct.THREAD_NUM
    just = ct.THREAD_NUM - remaind
    res = [1]
    for i in range(just):
        res.append(blocks * (i+1) + 1)
    for i in range(remaind):
        res.append(just * blocks + (blocks+1) * (i+1) + 1)
    return res
