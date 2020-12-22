'''常量'''
import json
import xlwt

CONFIG = json.load(open("config.json", "r"))
headers = CONFIG["headers"]
school = CONFIG["school"]
if headers["Cookie"] is None or school is None:
    headers["Cookie"] = input("请输入Cookie：")
    school = input("请输入学校：")
    with open("config.json", "w") as f:
        f.write(json.dumps(
            {"headers": headers, "school": school}, sort_keys=True, indent=4))
URL_PRE = "http://"+school+".pocketuni.net"
URL_TP = URL_PRE+"/index.php?app=event&mod=School&act=rank&k={type}&p={page}"
URL_USER = URL_PRE+"/index.php?app=home&mod=Account&act=index"

alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER
STYLE = xlwt.XFStyle()
STYLE.alignment = alignment
