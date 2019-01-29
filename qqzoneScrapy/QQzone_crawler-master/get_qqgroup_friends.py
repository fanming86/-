# get_qqgroup_friends.py



import requests
from time import sleep
import util
import json

class Get_friends_number(object):
    '''Use to get one's friends from their qzone's entry list'''

    def __init__(self):

        self.headers = util.headers
        self.base_url = util.qqgroups()
        print('Start to get friends list and save it for ./friends folder')

    def get_friends(self):
        url = self.base_url
        print("start get get_qqgroup_friends")
        print(url)
        res = requests.get(url, headers=self.headers)
        html = res.text
        flist = json.loads(html[10:-2])
        fl = flist['data']['friends']
        print(fl)

        # with open('qqgroupFriends.json','w',encoding='utf-8') as f:
        # 	f.write(html)

        if "请先登录" in html:
            print("登录失败，请检查原因")
            key = False

a = Get_friends_number()
print(a.get_friends())