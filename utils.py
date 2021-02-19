'''工具函数'''
import re

from constants import *
from loader import THREAD_NUM
from net import *


def get_num(string):
    '''使用正则表达式获得一个字符串中的数字'''
    return int(re.sub(r'\D', "", string))


def get_username():
    '''从个人信息页获取用户昵称'''
    user_page = get_bs_instance(URL_USER)
    return user_page.find(attrs={"name": "nickname"})["value"]


def get_rank_and_pages(type_: int):
    '''获取当前排名和总页数'''
    first_page = get_bs_instance(add_page(URL_TP.format(type=type_), 1))
    try:
        rank = get_num(first_page.find(class_="myrank").string)
    except AttributeError:
        rank = -1
    nodes = list(first_page.find(class_="page plist").children)
    pagecnt = int(nodes[6].string[2:])
    return rank, pagecnt


def divide_int(pages: int):
    '''将页数按线程数均分'''
    blocks = pages // THREAD_NUM
    remaind = pages % THREAD_NUM
    just = THREAD_NUM - remaind
    last = 1
    for i in range(just):
        tmp = blocks * (i+1) + 1
        yield (last, tmp)
        last = tmp
    for i in range(remaind):
        tmp = just * blocks + (blocks+1) * (i+1) + 1
        yield (last, tmp)
        last = tmp
