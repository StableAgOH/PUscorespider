'''数据可视化'''
import matplotlib.pyplot as plt
import seaborn as sns

import book


def data_show():
    '''直方图显示数据'''
    sns.histplot(book.load_data(), binwidth=5, kde=True)
    plt.show()
