'''常量'''
import datetime

# 错误信息
ERR_OPT = "错误：选项错误"
ERR_TYP = "错误：类型错误"
ERR_PGS = "错误：页数错误"
ERR_NRK = "错误：无法获取排名……"
# 普通信息
INFO_WELC = "欢迎亲爱的%s ━(*｀∀´*)ノ亻!"
INFO_RANK = "您当前的排名为：%d"
INFO_DONE = "任务完成啦！ヽ(￣▽￣)ﾉ"
# 输入提示语
QST_CTN = "数据已存在，是否继续爬取(Y/N)"
QST_TYP = "要爬取哪个类型的排名(1~3)："
QST_PAG = "共有%d页数据，要爬取几页数据(每页10个同学，0为爬取所有页)："
QST_DAN = "是否进行数据分析(Y/N)"

TYPES = ("", "月度排名", "学期排名", "学年排名")

TODAY = datetime.date.today()
BOOK_PATH = "books\\"+TODAY.strftime("%Y%m%d")+".xls"
