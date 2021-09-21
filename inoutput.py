'''获取用户输入的指令'''
import os
from colorama import init, Fore

from constants import *


def input_continue():
    '''是否需要继续爬取'''
    if os.path.exists(BOOK_PATH):
        if input_yn(QST_CTN) == 'Y':
            output_red(WARN_CTN)
            return True
        return False
    return True

def input_type():
    '''读入类型'''
    type_ = int(input(QST_TYP))
    while type_ < 1 or type_ > 3:
        output_red(ERR_TYP)
        type_ = int(input(QST_TYP))
    return type_


def input_pages(pagecnt: int):
    '''读入要爬取的页数'''
    pages = int(input(QST_PAG % pagecnt))
    while pages < 0 or pages > pagecnt:
        output_red(ERR_PGS)
        pages = int(input(QST_PAG % pagecnt))
    if pages == 0:
        pages = pagecnt
    return pages


def input_yn(info: str):
    '''获取用户输入的Y或N'''
    opt = input(info).upper()
    while opt not in ('Y', 'N'):
        output_red(ERR_OPT)
        opt = input(info).upper()
    return opt


init(autoreset=True, convert=True)


def output_red(string: str):
    '''以红色字体输出文本'''
    print(str(Fore.RED)+string)
