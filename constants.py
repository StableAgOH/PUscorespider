'''常量'''
import datetime
import colorama

QST_CTN = "数据已存在，是否继续爬取(Y/N)"
QST_TYP = "要爬取哪个类型的排名(1~3)："
QST_PAG = "共%d页，要爬取几页数据(0为爬取所有页)："
QST_DAN = "是否进行数据分析(Y/N)"
ERR_TPL = colorama.Fore.RED + "%s" + colorama.Fore.RESET
ERR_OPT = ERR_TPL % "错误：选项错误\n请输入正确的选项："
ERR_TYP = ERR_TPL % "错误：类型错误\n请输入正确的类型："
ERR_PGS = ERR_TPL % "错误：页数错误\n请输入正确的页数："
INFO_WELC = "欢迎亲爱的%s ━(*｀∀´*)ノ亻!"
INFO_RANK = "您当前的排名为：%d"
INFO_DONE = "任务完成啦！ヽ(￣▽￣)ﾉ"
TYPES = (None, "月度排名", "学期排名", "学年排名")

TODAY = datetime.date.today()
