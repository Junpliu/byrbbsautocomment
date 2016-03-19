#coding:utf-8
#北邮人论坛 bbs.byr.cn 发表评论脚本

import requests
from bs4 import BeautifulSoup
from config import *

class ByrbbsAutoComment(object):

    def __init__(self):
        self.s = requests.Session()
        
    def login(self,username,password):
        """
            username: 北邮人论坛账号
            password: 北邮人论坛密码
        """
        data = {"id":USERNAME,"passwd":PASSWORD}
        result = self.s.post("http://m.byr.cn/user/login",data)

    def comment(self,url,content):
        """
            url: 要评论帖子的url
            content: 评论内容
        """
        
        if url.endswith('/'):
            url = url[:-1]

        result = self.s.get(url)
        soup = BeautifulSoup(result.content)
        subject = soup.find_all('input',attrs={'name':'subject'})[0].attrs['value']

        thread_number = url.split('/')[-1]
        post_url = url[:-len(thread_number)]+"post/"+thread_number
        print post_url
        data = {"content":content,"subject":subject}
        result = self.s.post(post_url,data)


if __name__ == "__main__":
    ac = ByrbbsAutoComment()
    ac.login(USERNAME,PASSWORD)
    ac.comment(THREAD_URL,CONTENT)
    


