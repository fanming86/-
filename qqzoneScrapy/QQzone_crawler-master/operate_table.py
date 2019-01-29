#创建数据库
#**operate_table.py**：这个程序创建用于保存说说信息的数据库。
#里面写了创建数据表和删除数据表的两个函数。需要单独执行。
# 创建数据表：
# python operate_table.py create_table

import sqlite3
import sys

class Operate_table(object):

    def __init__(self):
        self.conn = sqlite3.connect('moods.sqlite')
        self.cur = self.conn.cursor()

    def create_table(self):
        sql = '''CREATE TABLE moods (
                 id integer primary key Autoincrement not null,
                 qq int not null,
                 content text null,
                 comment_count int not null,
                 ctime int not null,
                 phone text null,
                 image text null,
                 locate text null)'''
        self.cur.execute(sql)

    def drop_table(self):
        self.cur.execute('drop table moods')

if __name__ == '__main__':
    app = Operate_table()
    argv = sys.argv[1]
    try:
        eval("app.%s()" % argv)
    except Exception as e:
        print (e)
