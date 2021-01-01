'''工具函数'''
import os
import re
import book

import loader
import constants as ct


def get_num(string):
    '''使用正则表达式获得一个字符串中的数字'''
    return int(re.sub(r'\D', "", string))


def get_yn(info: str):
    '''获取用户输入的Y或N'''
    opt = input(info).upper()
    while opt not in ('Y', 'N'):
        opt = input(ct.ERR_OPT).upper()
    return opt


def whether_continue():
    '''是否需要继续爬取'''
    if os.path.exists(book.BOOK_PATH):
        if get_yn(ct.QST_CTN) == 'Y':
            return True
        return False
    return True


def divide_int(pages: int):
    '''将页数按线程数均分'''
    blocks = pages // loader.THREAD_NUM
    remaind = pages % loader.THREAD_NUM
    just = loader.THREAD_NUM - remaind
    last = 1
    for i in range(just):
        tmp = blocks * (i+1) + 1
        yield (last,tmp)
        last = tmp
    for i in range(remaind):
        tmp = just * blocks + (blocks+1) * (i+1) + 1
        yield (last,tmp)
        last = tmp
