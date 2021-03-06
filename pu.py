'''主模块'''
import tqdm

from constants import *
from datashower import data_show
from inoutput import *
from instances import workbook
from net import URL_TP
from utils import *

if __name__ == "__main__":
    if input_continue():
        output_red(WARN_CTN)
        for i in range(1, 4):
            print(str(i)+"."+TYPES[i])
        tp = input_type()
        url_pre = URL_TP.format(type=tp)
        rank, pagecnt = get_rank_and_pages(tp)
        workbook.write_title(tp)
        if rank != -1:
            print(INFO_RANK % rank)
        else:
            output_red(ERR_NRK)
        pages = input_pages(pagecnt)
        tr = tqdm.trange(1, pages+1, ascii=True)
        tr.set_description("进度")
        for page in tr:
            table = get_bs_instance(add_page(url_pre, page)).table
            data_page = [
                [
                    table.contents[stu].contents[attr].string
                    for attr in range(1, 8, 2)
                ]
                for stu in range(3, len(table.contents), 2)
            ]
            workbook.write_data(data_page)
        workbook.save()
    else:
        workbook.load_data()
    if input_yn(QST_DAN) == 'Y':
        data_show()
    print(INFO_DONE)
