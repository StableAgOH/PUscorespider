import os
from typing import List

import xlrd
import xlwt

from constants import BOOK_FOLDER, TODAY, BOOK_PATH, TYPES

al = xlwt.Alignment()
al.horz = xlwt.Alignment.HORZ_CENTER
al.vert = xlwt.Alignment.VERT_CENTER
STYLE = xlwt.XFStyle()
STYLE.alignment = al


class MyBook:
    def __init__(self):
        self.book = xlwt.Workbook(encoding="UTF-8")
        self.sheet: xlwt.Worksheet = self.book.add_sheet("PUscore")
        self.sheet.col(2).width = 2857
        self.write(1, ("排名", "姓名", "学号", "分数"))
        self.scores = []

    def save(self):
        if not os.path.exists(BOOK_FOLDER):
            os.makedirs(os.getcwd() + '\\' + BOOK_FOLDER)
        self.book.save(BOOK_PATH)

    def write(self, row, data: tuple):
        for col in range(4):
            self.sheet.write(row, col, data[col], STYLE)

    def write_data(self, data: List[List[int]]):
        for stu in data:
            ts = (int(stu[0]), str(stu[1]), str(stu[2]), float(stu[3]))  # rank, name, id, score
            self.write(int(stu[0]) + 1, ts)
            self.scores.append(float(stu[3]))

    def load_data(self):
        book = xlrd.open_workbook(BOOK_PATH)
        sheet = book.sheet_by_index(0)
        self.scores = sheet.col_values(3, 2)

    def write_title(self, type_):
        self.sheet.write_merge(
            0, 0, 0, 3, TODAY.strftime("%Y/%m/%d") + "  " + TYPES[type_], STYLE)


workbook = MyBook()
