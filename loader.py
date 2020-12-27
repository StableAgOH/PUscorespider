'''读取配置设置'''
import json
import os

if os.path.exists("config.json"):
    CONFIG = json.load(open("config.json", "r"))
    COOKIE = CONFIG["Cookie"]
    SCHOOL = CONFIG["school"]
    THREAD_NUM = CONFIG["thread_num"]
else:
    COOKIE = input("请输入Cookie：")
    SCHOOL = input("请输入学校：")
    THREAD_NUM = 16
    with open("config.json", "w") as f:
        f.write(json.dumps({"Cookie": COOKIE, "school": SCHOOL,
                            "thread_num": THREAD_NUM}, sort_keys=True, indent=4))
