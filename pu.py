'''主模块'''
import concurrent.futures
import tqdm

from constants import *
from datashower import data_show
from inoutput import *
from instances import workbook
from net import URL_TP, write_range
from utils import *

if __name__ == "__main__":
    if input_continue():
        print(INFO_WELC % get_username())
        for i in range(1, 4):
            print(str(i)+"."+TYPES[i])
        tp = input_type()
        url_pre = URL_TP.format(type=tp)
        rank, pagecnt = get_rank_and_pages(tp)
        workbook.write_title(tp)
        print(INFO_RANK % rank)
        pool = concurrent.futures.ThreadPoolExecutor()
        pages = input_pages(pagecnt)
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
    if input_yn(QST_DAN) == 'Y':
        data_show()
    print(INFO_DONE)
