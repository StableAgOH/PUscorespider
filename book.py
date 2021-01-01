'''工作簿相关'''
from typing import List, Tuple
import os
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
        self.scores = []
        self.done = 0

    def save(self):
        '''把工作簿保存到文件'''
        if not os.path.exists("books"):
            os.makedirs(os.getcwd()+"\\books")
        self.book.save(BOOK_PATH)

    def write(self, row: int, col: int, label):
        '''以STYLE为格式向sheet中写入数据'''
        self.sheet.write(row, col, label, STYLE)

    def write_data(self, data: List[List[int]]):
        '''向工作簿中写入数据'''
        for stu in data:
            rank, sno, name, score = \
                int(stu[0]), str(stu[1]), str(stu[2]), float(stu[3])
            self.write(rank+1, 0, rank)
            self.write(rank+1, 1, sno)
            self.write(rank+1, 2, name)
            self.write(rank+1, 3, score)
            self.scores.append(score)
        self.done += 1

    def write_title(self, type_):
        '''书写工作簿标题'''
        self.sheet.write_merge(
            0, 0, 0, 3, ct.TODAY.strftime("%Y/%m/%d") + "  " + ct.TYPES[type_], STYLE)
