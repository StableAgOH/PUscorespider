import datetime
from pathlib import Path

import xlrd
import xlwt

al = xlwt.Alignment()
al.horz = xlwt.Alignment.HORZ_CENTER
al.vert = xlwt.Alignment.VERT_CENTER
STYLE = xlwt.XFStyle()
STYLE.alignment = al

TODAY = datetime.date.today()


class MyBook:
    def __init__(self):
        self.folder = Path("books")
        self.path = self.folder / Path(f"{TODAY.strftime('%Y%m%d')}.xls")

        self.book = xlwt.Workbook(encoding="UTF-8")
        self.sheet = self.book.add_sheet("PUscore")
        self.sheet.col(2).width = 2857
        self.write(1, ("排名", "姓名", "学号", "分数"))
        self.scores = []

    def exists(self):
        return self.path.exists()

    def save(self):
        self.folder.mkdir(exist_ok=True)
        self.book.save(self.path)

    def write(self, row: int, data: tuple):
        for col in range(4):
            self.sheet.write(row, col, data[col], STYLE)

    def write_data(self, data: list[list[int]]):
        for stu in data:
            ts = (int(stu[0]), str(stu[1]), str(stu[2]), float(stu[3]))  # rank, name, id, score
            self.write(int(stu[0]) + 1, ts)
            self.scores.append(float(stu[3]))

    def load_data(self):
        sheet = xlrd.open_workbook(self.path).sheet_by_index(0)
        self.scores = sheet.col_values(3, 2)

    def write_title(self, tp: str):
        self.sheet.write_merge(0, 0, 0, 3, f"{TODAY.strftime('%Y/%m/%d')} {tp}", STYLE)
