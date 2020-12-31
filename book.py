'''工作簿相关'''
import os
import xlrd
import xlwt

import constants as ct


al = xlwt.Alignment()
al.horz = xlwt.Alignment.HORZ_CENTER
al.vert = xlwt.Alignment.VERT_CENTER
STYLE = xlwt.XFStyle()
STYLE.alignment = al
BOOK_PATH = "books\\"+ct.TODAY.strftime("%Y%m%d")+".xls"


class MyBook():
    '''进行操作的工作簿'''

    def __init__(self):
        self.book = xlwt.Workbook(encoding="UTF-8")
        self.sheet: xlwt.Worksheet = self.book.add_sheet("PUscore")
        self.sheet.col(2).width = 2857
        self.sheet.write(1, 0, "排名", STYLE)
        self.sheet.write(1, 1, "姓名", STYLE)
        self.sheet.write(1, 2, "学号", STYLE)
        self.sheet.write(1, 3, "分数", STYLE)

    def save(self):
        '''把工作簿保存到文件'''
        if not os.path.exists("books"):
            os.makedirs(os.getcwd()+"\\books")
        self.book.save(BOOK_PATH)

    def write_data(self, data: list):
        '''向工作簿中写入数据'''
        rank = int(data[0])
        self.sheet.write(rank+1, 0, rank, STYLE)
        self.sheet.write(rank+1, 1, data[1], STYLE)
        self.sheet.write(rank+1, 2, data[2], STYLE)
        self.sheet.write(rank+1, 3, float(data[3]), STYLE)

    def write_title(self, type_):
        '''书写工作簿标题'''
        self.sheet.write_merge(
            0, 0, 0, 3, ct.TODAY.strftime("%Y/%m/%d") + "  " + ct.TYPES[type_], STYLE)


def load_data():
    '''从已有的工作簿中读取数据'''
    book = xlrd.open_workbook(BOOK_PATH)
    sheet: xlrd.sheet.Sheet = book.sheets()[0]
    return sheet.col_values(3, 2)
