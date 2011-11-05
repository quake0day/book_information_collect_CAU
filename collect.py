#!/usr/local/bin/python
# -*- coding: utf8 -*-
import urllib,urllib2,cookielib
import re

class xiaobai:
    def __init__(self):
        self.UserName=''
        self.Password=''
        self.cookie=cookielib.CookieJar()
        self.opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        urllib2.install_opener(self.opener)
    def login(self,username,password):
        self.UserName=username
        _str=urllib.urlencode({'__VIEWSTATE=%2FwEPDwUKMTk4Njc5NTU4Mg9kFgICAw9kFgICBw8PZBYCHgdvbmNsaWNrBSdpZih0aGlzLmRpc2FibGVkPT1mYWxzZSl7cmV0dXJuICBiYygpO31kZP%2B9YQS1SQoVhX0gctevArgHvY9U&':'Tbusername':username,'Tbuserpwd':password,'RadioButtonList1':'login'})
## urlencode其实就是在URL后面加上“?user=username&mima=password”一类的东西，只不过用字典的方式可读性好一些
        #print _str
        _response=urllib2.urlopen('http://211.82.90.56:8080/caubook/TeacherLog.aspx?__VIEWSTATE=%2FwEPDwUKMTk4Njc5NTU4Mg9kFgICAw9kFgICBw8PZBYCHgdvbmNsaWNrBSdpZih0aGlzLmRpc2FibGVkPT1mYWxzZSl7cmV0dXJuICBiYygpO31kZP%2B9YQS1SQoVhX0gctevArgHvY9U&Tbusername=0607040101&Tbuserpwd=0607040101&RadioButtonList1=%E5%AD%A6%E7%94%9F&Button1=%E7%A1%AE%E8%AE%A4&__EVENTVALIDATION=%2FwEWBwKZqo6EDgKS6L7%2FCwK1gprrAQLo4%2BrNDQLN7c0VAveMotMNAoznisYGXMvRojLDcm7L2wkg34m0QFH3k5c%3D')
        _d=_response.read()
        _d = unicode(_d,'gb18030','ignore').encode('utf-8', 'ignore')
        #print _d
        if (re.search('欢迎您光临本站', _d)):
            return True
        else:
            return False
if __name__=="__main__":
        x=xiaobai()
        y=x.login('xxxx','xxxxx')
        print y
