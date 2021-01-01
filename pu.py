'''主模块'''
import tqdm
from utils import *
from constants import *
from thread import DataThread
from datashower import data_show
from net import get_username, get_rank_and_pages
from instances import workbook

if __name__ == "__main__":
    if whether_continue():
        print(INFO_WELC % get_username())
        for i in range(1, 4):
            print(str(i)+"."+TYPES[i])
        tp = int(input(QST_TYP))
        while tp < 1 or tp > 3:
            tp = int(input(ERR_TYP))
        rank, pagecnt = get_rank_and_pages(tp)
        print(INFO_RANK % rank)
        pages = int(input(QST_PAG % pagecnt))
        if pages == 0:
            pages = pagecnt
        while pages < 0 or pages > pagecnt:
            pages = int(input(ERR_PGS))
        workbook.write_title(tp)
        divide = divide_int(pages)
        for i in range(len(divide)-1):
            t = DataThread(tp, divide[i], divide[i+1])
            t.start()
        with tqdm.tqdm(total=pages, ascii=True) as pbar:
            pbar.set_description("进度")
            LAST = 0
            DONE = len(workbook.scores) // 10
            while DONE != pages:
                pbar.update(DONE-LAST)
                LAST = DONE
                DONE = len(workbook.scores) // 10
            pbar.update(pages-LAST)
        workbook.save()
    if get_yn(QST_DAN) == 'Y':
        data_show()
    print(INFO_DONE)
