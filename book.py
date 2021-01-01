'''工作簿相关'''
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

    def save(self):
        '''把工作簿保存到文件'''
        self.book.save(BOOK_PATH)

    def write(self, row: int, col: int, label):
        '''以STYLE为格式向sheet中写入数据'''
        self.sheet.write(row, col, label, STYLE)

    def write_data(self, data: list):
        '''向工作簿中写入数据'''
        rank, sno, name, score = \
            int(data[0]), str(data[1]), str(data[2]), float(data[3])
        self.write(rank+1, 0, rank)
        self.write(rank+1, 1, sno)
        self.write(rank+1, 2, name)
        self.write(rank+1, 3, score)
        self.scores.append(score)

    def write_title(self, type_):
        '''书写工作簿标题'''
        self.sheet.write_merge(
            0, 0, 0, 3, ct.TODAY.strftime("%Y/%m/%d") + "  " + ct.TYPES[type_], STYLE)
