'''读取配置设置'''
import json
import os

if os.path.exists("config.json"):
    CONFIG = json.load(open("config.json", "r"))
    COOKIE = CONFIG["Cookie"]
    SCHOOL = CONFIG["school"]
    RETRIES = CONFIG["max_retries"]
    TIMEOUT = CONFIG["timeout"]
else:
    COOKIE = input("请输入Cookie：")
    SCHOOL = input("请输入学校：")
    RETRIES = 5
    TIMEOUT = 60
    json.dump({"Cookie": COOKIE, "school": SCHOOL,
               "max_retries": RETRIES, "timeout": TIMEOUT}, open("config.json", "w"), sort_keys=True, indent=4)
