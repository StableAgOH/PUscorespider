'''数据可视化'''
import matplotlib.pyplot as plt
import seaborn as sns
from book import load_data

def data_show():
    '''直方图显示数据'''
    sns.histplot(load_data(), kde=True)
    plt.show()
