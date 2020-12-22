'''工具函数'''
import re
import requests
import bs4
import xlwt
import constants as ct


def get_rq(url: str):
    '''从url获取一个get的requests'''
    return requests.get(url, headers=ct.headers)


def init_bs(url: str):
    '''从url获取一个BeautifulSoup的实例'''
    return bs4.BeautifulSoup(get_rq(url).content, "lxml")


def get_num(string: bs4.NavigableString):
    '''使用正则表达式获得一个NavigableString中的数字'''
    return int(re.sub(r"\D", "", string))


def init_book():
    '''初始化工作簿'''
    book = xlwt.Workbook(encoding="UTF-8")
    sheet: xlwt.Worksheet = book.add_sheet("PUscore")
    sheet.col(2).width = 2857
    sheet.write(0, 0, label="排名", style=ct.STYLE)
    sheet.write(0, 1, label="姓名", style=ct.STYLE)
    sheet.write(0, 2, label="学号", style=ct.STYLE)
    sheet.write(0, 3, label="分数", style=ct.STYLE)
    return book, sheet


def write_data(sheet: xlwt.Worksheet, elements: list):
    '''向sheet中写入elements中的数据'''
    rank = int(elements[0].string)
    sheet.write(rank, 0, label=rank, style=ct.STYLE)
    sheet.write(rank, 1, label=elements[1].string, style=ct.STYLE)
    sheet.write(rank, 2, label=elements[2].string, style=ct.STYLE)
    sheet.write(rank, 3, label=float(elements[3].string), style=ct.STYLE)


def get_rank_and_pages(type_: int):
    '''获取当前排名和总页数'''
    first_page = init_bs(ct.URL_TP.format(type=type_, page='1'))
    rank = get_num(first_page.find(class_="myrank").string)
    nodes = []
    for i in first_page.find(class_="page plist").children:
        nodes.append(i)
    pagecnt = int(nodes[6].string[2:])
    return rank, pagecnt
