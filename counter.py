'''计数器'''


class Counter():
    '''用于统计线程工作进度的计数器'''

    def __init__(self) -> None:
        self.cnt = 0
        self.end = 0
        self.last = 0

    def increment(self):
        '''增加1'''
        self.cnt += 1

    def done(self):
        '''计数器是否记满'''
        return self.cnt == self.end

    def get_end(self):
        '''获取计数器最大值'''
        return self.end

    def set_end(self, end: int):
        '''设置计数器最大值'''
        self.end = end

    def get_cnt(self):
        '''获取计数器数值'''
        return self.cnt

    def get_diff(self):
        '''获取计数器当前值与上次值的差值'''
        ret = self.cnt-self.last
        self.last = self.cnt
        return ret
