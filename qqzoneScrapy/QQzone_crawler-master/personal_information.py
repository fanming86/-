#获取好友个人信息，保存在persionInfo目录下

from urllib import parse
import util
import requests
import json

def getInfo(friendqq):
	header = util.headers
	cookie = header['Cookie']
	qq_start = cookie.find('uin=o')
	qq_end = cookie.find(';', qq_start)
	qqnumber = cookie[qq_start+5 : qq_end]
	if qqnumber[0] == 0:
	    qqnumber = qqnumber[1:]


	host = 'https://h5.qzone.qq.com/proxy/domain/base.qzone.qq.com/cgi-bin/user/cgi_userinfo_get_all?'
	params = {
	'uin':friendqq,
	'vuin':qqnumber,
	'g_tk':util.g_tk
	}

	url = host + parse.urlencode(params)
	print (url)
	resp = requests.get(url,headers = util.headers)
	print (resp.text)

	util.check_path('persionInfo')
	 
	with open('persionInfo/info'+friendqq,'w',encoding='utf-8') as f:
		f.write(resp.text)



with open('qqnumber.inc',encoding='utf-8') as f:
	content = f.read()
	contents = eval(content)


while contents != []:
    save_back_qnumber = contents[:]
    item = contents.pop()
    qq = item['data']
    print("Dealing with:\t%s" % qq)
    getInfo(qq)



