'''主模块'''
import tqdm
from utils import *
from constants import *

if __name__ == "__main__":
    user_name = init_bs(URL_USER).find(attrs={"name": "nickname"})["value"]
    print("欢迎亲爱的%s ━(*｀∀´*)ノ亻!" % user_name)
    print("1.月度排名\t2.学期排名\t3.学年排名")
    type_ = int(input("要爬取哪个类型的排名："))
    while type_ < 1 or type_ > 3:
        type_ = int(input("\033[5;31;40m错误：类型错误\n请输入正确的类型：\033[0m"))
    rank, pagecnt = get_rank_and_pages(type_)
    print("您当前的排名为：%d" % rank)
    pages = int(input("共%d页，要爬取几页数据？" % pagecnt))
    book, sheet = init_book()
    for page in tqdm.tqdm(range(1, pages+1)):
        bs = init_bs(URL_TP.format(type=type_, page=page))
        node = bs.tr.next_sibling.next_sibling
        while node:
            elements = node.find_all("td")
            write_data(sheet, elements)
            node = node.next_sibling.next_sibling
    book.save("PUscore.xls")
