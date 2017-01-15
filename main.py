# -*- coding:utf-8 -*-
import re
import sys
import urllib
import chardet

def getHtml(url):
     page = urllib.urlopen(url)
     html = page.read()
     return html

def getHtmlEncoding(url):
     code = chardet.detect(url)['encoding']
     # print "html is encoding by:", code
     # utf-8
     return code

def getPrintHtmlEncoding(url):
     code = getHtmlEncoding(url)
     sysCode = sys.getfilesystemencoding()
     url = url.decode(code).encode(sysCode)
     return url
     # type(html): str

def getServerAddr(url):
     # 得到三个服务器地址
     print url
     # TODO 已不能用iss作为匹配规则
     addr = r"\w+\.iss\.\w"
     t = re.compile(addr)
     addr = re.findall(t, url)
     print addr
     return addr

def getPort(url):
     # 得到三个端口
     tmp = "端口".decode('utf-8').encode('gbk')
     # TODO 最好不用数字匹配
     port = r":\d+</h4>"
     port = tmp + port
     t = re.compile(port)
     port = re.findall(t, url)
     # 测试port列表中变量的编码类型
     # codeTmp = chardet.detect(port[0])[‘encoding‘]
     # print codeTmp
     for i in range(len(port)):
         Tmp = "\d+"
         t1 = re.compile(Tmp)
         t2 = re.findall(t1, port[i])
         port[i] = t2[0]
     print port
     return port

def getPasswd(url):
     # 得到密码
     # TODO 最好不用数字匹配
     passwd = r":\d{8}<"
     t = re.compile(passwd)
     passwd = re.findall(t, url)
     for i in range(len(passwd)):
         Tmp = r'\d+'
         t1 = re.compile(Tmp)
         t2 = re.findall(t1, passwd[i])
         passwd[i] = t2[0]
     print passwd
     return passwd

def getEncryptWay(url):
     # 得到加密方式
     EncryptWay = r"[A-Za-z]+-\d+-[A-Za-z]+"
     t = re.compile(EncryptWay)
     EncryptWay = re.findall(t, url)
     return EncryptWay


html = getHtml("http://www.ishadowsocks.me/")
html = getPrintHtmlEncoding(html)

serverAddr = getServerAddr(html)
port = getPort(html)
passwd = getPasswd(html)
EncryptWay = getEncryptWay(html)
info = ['服务器地址：', '端口：', '密码：','加密方式：']

if __name__ == '__main__':
     for i in range(len(serverAddr)):
         print info[0].decode('utf-8').encode('gbk'), serverAddr[i]
         print info[1].decode('utf-8').encode('gbk'), port[i]
         print info[2].decode('utf-8').encode('gbk'), passwd[i]
         print info[-1].decode('utf-8').encode('gbk'), EncryptWay[i]
         print
     raw_input("> ")
