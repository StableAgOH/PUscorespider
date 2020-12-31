'''数据可视化'''
import matplotlib.pyplot as plt
import seaborn as sns

import book
import loader


def data_show():
    '''直方图显示数据'''
    sns.histplot(book.load_data(), binwidth=4, kde=True)
    plt.title(loader.SCHOOL+" PU Score", fontproperties="Consolas")
    plt.xlabel("Score", fontproperties="Consolas")
    plt.ylabel("Number of students", fontproperties="Consolas")
    plt.show()
