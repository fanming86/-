#**get_my_friends.py**： 用于从QQ空间服务器获取包括自己的QQ好友信息的文件，
#其中包括他们的QQ号和名称（此处是备注名），保存到本地，每个文件中保存有50个。
#每完成一个文件请求后，会暂停5秒。在程序运行时，会自动将这些文件保存在friends文件夹中。


import requests
from time import sleep
import util

class Get_friends_number(object):
    '''Use to get one's friends from their qzone's entry list'''

    def __init__(self):

        self.headers = util.headers
        self.base_url = util.parse_friends_url()
        util.check_path('friends')
        print('Start to get friends list and save it for ./friends folder')

    def get_friends(self):

        key = True
        position = 0
        while key:
            url = self.base_url + '&offset=' + str(position)
            referer = 'http://qzs.qq.com/qzone/v8/pages/setting/visit_v8.html'
            self.headers['Referer'] = referer

            print("\tDealing with position\t%d." % position)
            print(url)  #获取好友列表的地址
            res = requests.get(url, headers=self.headers)
            html = res.text
            print(html)
            with open('friends/offset' + str(position) + '.json', 'w',encoding='utf-8') as f:
                f.write(html)

            with open('friends/offset' + str(position) + '.json',encoding='utf-8') as f2:
                con = f2.read()

            if "请先登录" in con:
                print("登录失败，请检查原因")
                key = False
                break
            if '''"uinlist":[]''' in con:
                print("Get friends Finish")
                break
                key = False

            position += 50
            sleep(5)



# a = Get_friends_number()
# print(a.get_friends())