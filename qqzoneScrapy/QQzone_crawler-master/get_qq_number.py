#获取所有的好友，此脚本是处理get_my_friends.py文件，处理该文件产生的结果，将所有好友存放在qqnumber.inc文件中
#**get_qq_number.py**： 用于从上一步保存好的文件中提取出所有好友的QQ号和名称，
#QQ号和名称以字典形式保存，再以它们组成的字典为作元素构造列表，再保存到本地，文件名为qqnumber.inc

import json
import os

class exact_data_from_result(object):
    '''Define method to get my qq friends data from result
       and get my mood data from result'''

    def __init__(self):
        print("Start to exact the qq number item from get_friends result")

    def exact_qq_number(self):
        '''Get qq number data from json file'''
        friendsFiles = [x for x in os.listdir('friends') if x.endswith("json")]

        qqnumber_item = []
        i = 0
        for each_file in friendsFiles:
            with open('friends/' + each_file,encoding='utf-8') as f:
                source = f.read()
                con_dict = source[75:-4].replace('\n', '')
                con_json = json.loads(con_dict)
                friends_list = con_json['uinlist']

                # Get each item from friends list, each item is a dict
                for item in friends_list:
                    i = i + 1
                    qqnumber_item.append(item)
        else:
            with open('qqnumber.inc', 'w',encoding='utf-8') as qqfile:
                qqfile.write(str(qqnumber_item))

# a = exact_data_from_result()
# a.exact_qq_number()