'''数据可视化'''
import matplotlib.pyplot as plt
import seaborn as sns

from instances import workbook


def data_show():
    '''直方图显示数据'''
    sns.histplot(workbook.scores, binwidth=5, kde=True)
    plt.show()
