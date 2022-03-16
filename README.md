# PUscorespider

获取 PU 口袋校园的分数排行榜，并可以进行直方图数据分析，为各位团支书/班长的工作提供便利。

![](https://user-images.githubusercontent.com/50107074/157648310-dfa3b708-9238-4687-a2bc-e9f7acf6c240.png)

多线程应该是被 PU 限速了，已改为单线程。

在使用前请先运行以下指令以安装所需的包。

```bash
pip install -r requirements.txt
```

运行 pu.py 即可在 books 目录下获取保存了数据的工作簿一份，首次运行需输入学校缩写、手机号码和密码，手机号码和密码用来获取用户当前排名及其他同学的学号信息。

学校缩写获得方法：

1. 访问 [PU 口袋校园官网](http://www.pocketuni.net/)
2. 在网页右上角“登录入口”处登录
3. 在地址栏中即可找到学校缩写

## 待实现功能

1. 在同一文件的多个 sheet 中爬取多个类型的数据
