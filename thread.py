'''线程'''
import threading
from typing import List

from book import workbook

class DataThread(threading.Thread):
    '''读写数据线程'''

    def __init__(self, begin, end):
        threading.Thread.__init__(self)
        self.begin = begin
        self.end = end

    def run(self):
        workbook.write_data(self.begin, self.end)

def start_all(threadlist:List[threading.Thread]):
    '''开始threadlist里的所有线程'''
    for thread in threadlist:
        thread.start()
