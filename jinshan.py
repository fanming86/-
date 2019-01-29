
import requests
import json
import time
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
'Referer':'http://www.iciba.com/'}
url = 'http://sentence.iciba.com/index.php?callback=jQuery19003480623426505034_%s&c=dailysentence&m=getTodaySentence&_=1525013686688' % int(time.time()*1000)
res = requests.get(url,headers=headers)
aaa = res.text[41:-1]
rrrr = json.loads(aaa)
print (rrrr['note'])

# url = 'http://open.iciba.com/dsapi'
# res = requests.get(url)
# rrr = json.loads(res.text)
# print (rrr['note'])