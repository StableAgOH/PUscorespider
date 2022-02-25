import os
import re

import seaborn as sns
from colorama import Fore, init
from matplotlib import pyplot as plt

import loader
from book import workbook
from constants import *
from net import *


def get_num(string):
    return int(re.sub(r'\D', "", string))


def get_rank_and_pages(type_: int):
    first_page = get_bs_instance(add_page(URL_TP.format(type=type_), 1))
    try:
        rank = get_num(first_page.find(class_="myrank").string)
    except AttributeError:
        rank = -1
    nodes = list(first_page.find(class_="page plist").children)
    pagecnt = int(nodes[6].string[2:])
    return rank, pagecnt


def input_continue():
    if os.path.exists(BOOK_PATH):
        if input_yn(QST_CTN) == 'Y':
            output_red(WARN_CTN)
            return True
        return False
    return True


def input_type():
    type_ = int(input(QST_TYP))
    while type_ < 1 or type_ > 3:
        output_red(ERR_TYP)
        type_ = int(input(QST_TYP))
    return type_


def input_pages(pagecnt: int):
    pages = int(input(QST_PAG % pagecnt))
    while pages < 0 or pages > pagecnt:
        output_red(ERR_PGS)
        pages = int(input(QST_PAG % pagecnt))
    if pages == 0:
        pages = pagecnt
    return pages


def input_yn(info: str):
    opt = input(info).upper()
    while opt not in ('Y', 'N'):
        output_red(ERR_OPT)
        opt = input(info).upper()
    return opt


init(autoreset=True, convert=True)


def output_red(string: str):
    print(str(Fore.RED) + string)


def show():
    sns.histplot(workbook.scores, binwidth=4, kde=True)
    plt.title(loader.SCHOOL + " PU Score", fontproperties="Consolas")
    plt.xlabel("Score", fontproperties="Consolas")
    plt.ylabel("Number of students", fontproperties="Consolas")
    plt.show()
