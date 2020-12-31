'''主模块'''
import tqdm
from utils import whether_continue,divide_int,get_yn
from constants import *
from thread import DataThread
from datashower import data_show
from net import get_username, get_rank_and_pages
from instances import cter, workbook

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
        cter.set_end(pages)
        divide = divide_int(pages)
        for i in range(len(divide)-1):
            t = DataThread(tp, divide[i], divide[i+1])
            t.start()
        with tqdm.tqdm(total=cter.get_end(), ascii=True) as pbar:
            while not cter.done():
                pbar.update(cter.get_diff())
            pbar.update(cter.get_diff())
        workbook.save()
    if get_yn(QST_DAN) == 'Y':
        data_show()
    print(INFO_DONE)
