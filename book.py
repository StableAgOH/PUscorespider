'''工作簿相关'''
from typing import List
import os
import xlwt
import xlrd

from constants import TODAY, BOOK_PATH, TYPES


al = xlwt.Alignment()
al.horz = xlwt.Alignment.HORZ_CENTER
al.vert = xlwt.Alignment.VERT_CENTER
STYLE = xlwt.XFStyle()
STYLE.alignment = al


class MyBook():
    '''进行操作的工作簿'''

    def __init__(self):
        self.book = xlwt.Workbook(encoding="UTF-8")
        self.sheet: xlwt.Worksheet = self.book.add_sheet("PUscore")
        self.sheet.col(2).width = 2857
        self.write(1, 0, "排名")
        self.write(1, 1, "姓名")
        self.write(1, 2, "学号")
        self.write(1, 3, "分数")
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

    def load_data(self):
        '''从已有的工作簿中读取数据'''
        book = xlrd.open_workbook(BOOK_PATH)
        sheet = book.sheet_by_index(0)
        self.scores = sheet.col_values(3,2)

    def write_title(self, type_):
        '''书写工作簿标题'''
        self.sheet.write_merge(
            0, 0, 0, 3, TODAY.strftime("%Y/%m/%d") + "  " + TYPES[type_], STYLE)
