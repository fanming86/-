import requests
from time import sleep
import util
import json

cookie = util.get_cookie()
g_tk = util.get_g_tk()

url = 'https://h5.qzone.qq.com/proxy/domain/m.qzone.qq.com/cgi-bin/new/add_msgb?g_tk='
url += str(g_tk)

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Cookie': cookie,
            'content-type':'application/json',
        }

d = {'content': '哈喽',
'hostUin': '969756850',
'uin': '961118830',
'g_tk': g_tk}

d = json.dumps(d)

res = requests.post(url,data=d,headers=header)

print(res,res.text)
