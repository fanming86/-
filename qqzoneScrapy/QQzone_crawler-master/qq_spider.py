#coding:utf-8
from  selenium import webdriver
import requests
import time
import os
from urllib import parse
import configparser

class Spider(object):
    def __init__(self):
        self.web=webdriver.Chrome()
        self.web.get('https://user.qzone.qq.com')
        config = configparser.ConfigParser(allow_no_value=False)
        config.read('userinfo.ini')
        self.__username =config.get('qq_info','qq_number')
        self.__password=config.get('qq_info','qq_password')
        self.headers={
                'host': 'h5.qzone.qq.com',
                'accept-encoding':'gzip, deflate, br',
                'accept-language':'zh-CN,zh;q=0.8',
                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
                'connection': 'keep-alive'
        }
        self.req=requests.Session()
        self.cookies={}

    

    def login(self):
        self.web.switch_to_frame('login_frame')
        log=self.web.find_element_by_id("switcher_plogin")
        log.click()
        time.sleep(1)
        username=self.web.find_element_by_id('u')
        username.send_keys(self.__username)
        ps=self.web.find_element_by_id('p')
        ps.send_keys(self.__password)
        btn=self.web.find_element_by_id('login_button')
        time.sleep(1)
        btn.click()
        time.sleep(2)
        self.web.get('https://user.qzone.qq.com/{}'.format(self.__username))
        cookie=''
        for elem in self.web.get_cookies():
            cookie+=elem["name"]+"="+ elem["value"]+";"
        self.cookies=cookie
        print(cookie)
        with open('cookie_file','w') as f:
            f.write(cookie)
        self.get_g_tk()
        self.headers['Cookie']=self.cookies
        self.web.quit()
        
    
    def get_frends_url(self):
        url='https://h5.qzone.qq.com/proxy/domain/base.qzone.qq.com/cgi-bin/right/get_entryuinlist.cgi?'
        params = {"uin": self.__username,
              "fupdate": 1,
              "action": 1,
              "g_tk": self.g_tk}
        url = url + parse.urlencode(params)
        return url

    def get_frends_num(self):
        t=True
        offset=0
        url=self.get_frends_url()
        while(t):
            url_=url+'&offset='+str(offset)
            page=self.req.get(url=url_,headers=self.headers)
            if "\"uinlist\":[]" in page.text:
                t=False
            else:
                if not os.path.exists("./frends/"):
                    os.mkdir("frends/")
                with open('./frends/'+str(offset)+'.json','w',encoding='utf-8') as w:
                    w.write(page.text)
                offset += 50


    def get_g_tk(self):
        p_skey = self.cookies[self.cookies.find('p_skey=')+7: self.cookies.find(';', self.cookies.find('p_skey='))]
        h=5381
        for i in p_skey:
            h+=(h<<5)+ord(i)
        print('g_tk',h&2147483647)
        self.g_tk=h&2147483647


        

if __name__=='__main__':
    sp=Spider()
    sp.login()
    # sp.get_frends_num()
    # from data_analys import dataToExcel
