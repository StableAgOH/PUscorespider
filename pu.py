'''主模块'''
import concurrent.futures
import tqdm
from utils import *
from constants import *
from datashower import data_show
from net import URL_TP, get_username, get_rank_and_pages, write_range
from instances import workbook

if __name__ == "__main__":
    if whether_continue():
        print(INFO_WELC % get_username())
        for i in range(1, 4):
            print(str(i)+"."+TYPES[i])
        tp = int(input(QST_TYP))
        while tp < 1 or tp > 3:
            tp = int(input(ERR_TYP))
        url_pre = URL_TP.format(type=tp)
        rank, pagecnt = get_rank_and_pages(tp)
        print(INFO_RANK % rank)
        pages = int(input(QST_PAG % pagecnt))
        while pages < 0 or pages > pagecnt:
            pages = int(input(ERR_PGS))
        if pages == 0:
            pages = pagecnt
        workbook.write_title(tp)
        pool = concurrent.futures.ThreadPoolExecutor()
        for rg in divide_int(pages):
            pool.submit(write_range, url_pre, *rg)
        with tqdm.tqdm(total=pages, ascii=True) as pbar:
            pbar.set_description("进度")
            LAST = 0
            DONE = workbook.done
            while DONE != pages:
                pbar.update(DONE-LAST)
                LAST = DONE
                DONE = workbook.done
            pbar.update(pages-LAST)
        pool.shutdown()
        workbook.save()
    if get_yn(QST_DAN) == 'Y':
        data_show()
    print(INFO_DONE)
