'''线程'''
import threading

import net
from instances import workbook


class DataThread(threading.Thread):
    '''读写数据线程'''

    def __init__(self, type_, begin, end):
        threading.Thread.__init__(self)
        self.url = net.URL_TP.format(type=type_)
        self.begin = begin
        self.end = end

    def run(self):
        for page in range(self.begin, self.end):
            table = net.get_bs_instance(net.add_page(self.url, page)).table
            for i in range(3, len(table.contents), 2):
                workbook.write_data([table.contents[i].contents[j].string
                                     for j in range(1, 8, 2)])
