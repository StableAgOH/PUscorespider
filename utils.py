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


def init_book(type_: int):
    '''初始化工作簿'''
    book = xlwt.Workbook(encoding="UTF-8")
    sheet: xlwt.Worksheet = book.add_sheet("PUscore")
    sheet.col(2).width = 2857
    sheet.write_merge(
        0, 0, 0, 3, ct.today.strftime("%Y/%m/%d") + "  " + ct.types[type_], ct.STYLE)
    sheet.write(1, 0, "排名", ct.STYLE)
    sheet.write(1, 1, "姓名", ct.STYLE)
    sheet.write(1, 2, "学号", ct.STYLE)
    sheet.write(1, 3, "分数", ct.STYLE)
    return book, sheet


def write_data(sheet: xlwt.Worksheet, elements: list):
    '''向sheet中写入elements中的数据'''
    rank = int(elements[0].string)
    sheet.write(rank+1, 0, rank, ct.STYLE)
    sheet.write(rank+1, 1, elements[1].string, ct.STYLE)
    sheet.write(rank+1, 2, elements[2].string, ct.STYLE)
    sheet.write(rank+1, 3, float(elements[3].string), ct.STYLE)


def get_rank_and_pages(type_: int):
    '''获取当前排名和总页数'''
    first_page = init_bs(ct.URL_TP.format(type=type_, page='1'))
    rank = get_num(first_page.find(class_="myrank").string)
    nodes = []
    for i in first_page.find(class_="page plist").children:
        nodes.append(i)
    pagecnt = int(nodes[6].string[2:])
    return rank, pagecnt
