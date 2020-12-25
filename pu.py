'''主模块'''
import time
import tqdm
from utils import *
from constants import *
from book import workbook
from thread import *
from datashower import *
from counter import cter

if __name__ == "__main__":
    if whether_continue():
        user_name = init_bs(URL_USER).find(attrs={"name": "nickname"})["value"]
        print(INFO_WELC % user_name)
        for i in range(1, 4):
            print(str(i)+"."+TYPES[i])
        type_ = int(input(QST_TYP))
        while type_ < 1 or type_ > 3:
            type_ = int(input(ERR_TYP))
        rank, pagecnt = get_rank_and_pages(type_)
        print(INFO_RANK % rank)
        pages = int(input(QST_PAG % pagecnt))
        if pages == 0:
            pages = pagecnt
        while pages < 0 or pages > pagecnt:
            pages = int(input(ERR_PGS))
        workbook.write_title(type_)
        cter.set_end(pages)
        divide = divide_int(pages)
        ts = [DataThread(divide[i], divide[i+1])
              for i in range(len(divide)-1)]
        start_all(ts)
        with tqdm.tqdm(total=cter.get_end(),ascii=True) as pbar:
            while not cter.done():
                pbar.update(cter.get_diff())
                time.sleep(0.1)
            pbar.update(cter.get_diff())
        workbook.save()
    opt = get_yn(QST_DAN)
    if opt == 'Y':
        data_show()
    print(INFO_DONE)
