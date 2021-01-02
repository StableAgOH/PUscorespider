'''工具函数'''
import re

from constants import *
from loader import THREAD_NUM


def get_num(string):
    '''使用正则表达式获得一个字符串中的数字'''
    return int(re.sub(r'\D', "", string))


def divide_int(pages: int):
    '''将页数按线程数均分'''
    blocks = pages // THREAD_NUM
    remaind = pages % THREAD_NUM
    just = THREAD_NUM - remaind
    last = 1
    for i in range(just):
        tmp = blocks * (i+1) + 1
        yield (last, tmp)
        last = tmp
    for i in range(remaind):
        tmp = just * blocks + (blocks+1) * (i+1) + 1
        yield (last, tmp)
        last = tmp
