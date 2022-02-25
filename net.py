import requests
import requests.adapters
import bs4

from loader import SCHOOL, COOKIE, RETRIES, TIMEOUT

URL_PRE = "https://"+SCHOOL+".pocketuni.net"
URL_TP = URL_PRE+"/index.php?app=event&mod=School&act=rank&k={type}"
URL_USER = URL_PRE+"/index.php?app=home&mod=Account&act=index"

HEADERS = {
    "Accept": "text/html",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/87.0.4280.88 Safari/537.36",
    "Connection": "close",
    "Cookie": COOKIE
}


def get_res(url: str):
    ses = requests.session()
    ses.mount("https://", requests.adapters.HTTPAdapter(max_retries=RETRIES))
    return ses.get(url, headers=HEADERS, timeout=TIMEOUT)


def get_bs_instance(url: str):
    return bs4.BeautifulSoup(get_res(url).content, "lxml")


def add_page(url: str, page: int):
    return url+"&p="+str(page)
