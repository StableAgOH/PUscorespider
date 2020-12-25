'''常量'''
import json
import datetime

CONFIG = json.load(open("config.json", "r"))
headers = CONFIG["headers"]
school = CONFIG["school"]
if headers["Cookie"] is None or school is None:
    headers["Cookie"] = input("请输入Cookie：")
    school = input("请输入学校：")
    with open("config.json", "w") as f:
        f.write(json.dumps(
            {"headers": headers, "school": school}, indent=4))

URL_PRE = "http://"+school+".pocketuni.net"
URL_TP = URL_PRE+"/index.php?app=event&mod=School&act=rank&k={type}&p={page}"
URL_USER = URL_PRE+"/index.php?app=home&mod=Account&act=index"

QST_CTN = "数据已存在，是否继续爬取(Y/N)"
QST_TYP = "要爬取哪个类型的排名(1~3)："
QST_PAG = "共%d页，要爬取几页数据(0为爬取所有页)："
QST_DAN = "是否进行数据分析(Y/N)"
ERR_OPT = "\033[5;31;40m错误：选项错误\n请输入正确的选项：\033[0m"
ERR_TYP = "\033[5;31;40m错误：类型错误\n请输入正确的类型：\033[0m"
ERR_PGS = "\033[5;31;40m错误：页数错误\n请输入正确的页数：\033[0m"
INFO_WELC = "欢迎亲爱的%s ━(*｀∀´*)ノ亻!"
INFO_RANK = "您当前的排名为：%d"
INFO_DONE = "任务完成啦！ヽ(￣▽￣)ﾉ"

TYPES = (None, "月度排名", "学期排名", "学年排名")
TODAY = datetime.date.today()

THREAD_NUM = CONFIG["thread_num"]
