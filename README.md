# PUscorespider

AgOH的首个爬虫作品，多线程快速爬取PU口袋校园的分数排行榜，并可以进行直方图数据分析

![](https://s3.ax1x.com/2020/12/27/r4Ipmd.png)

在使用前请先运行以下指令以安装所需的包

```Python
pip install -r requirements.txt
```

运行pu.py即可在books目录下获取保存了数据的工作簿一份，首次运行需输入学校缩写及Cookie

* Cookie获得方法：请自行百度
* 学校缩写获得方法：
  1. 访问[PU口袋校园官网](http://www.pocketuni.net/)
  2. 在网页右上角“登录入口”处登录
  3. 在地址栏中即可找到学校缩写

## 待实现功能

1. 在同一文件的多个sheet中爬取多个类型的数据
