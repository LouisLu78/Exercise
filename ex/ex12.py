# -*- coding:utf-8 -*-
import re
# message='My mobile number is 86-13966666666.'
# # mobile_regre=re.compile(r'\d\d-\d\d\d\d\d\d\d\d\d\d\d')
# # mobile_regre=re.compile(r'(\d){2}-(\d){11}')
# mobile_regre=re.compile(r'(\d){1,3}-(\d){9,12}')
# mobile_regre1=re.compile(r'(\d){1,3}-(\d){9,12}?')
# mo=mobile_regre.search(message)
# mo1=mobile_regre1.search(message)
# print(mo.group())
# print(mo1.group())

# import requests
# Appel=requests.get('https://m.runoob.com/manual/pythontutorial3/docs/html/index.html')
# a=Appel.text
# # print(a)
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(a,'html.parser')
# print(soup.p)

# s='Today is hot'
# print(s.find('o'))
# s_re=re.compile(r'o')
# mo=s_re.findall(s)
# print(mo)
# a={1,5,7,9.1,5}
# print(set(a))
#
# Logo_code = { 'BIDU':'Baidu', 'SINA':'Sina', 'YOKU':'Youku' }
# print(Logo_code.keys())
# print(Logo_code['YOKU'])
# print (len(Logo_code))

# for i in range(6,12,2):
#  print(i)
# print(range(6,12,2),'finish')
#
# a = ['i', 'love', 'coding', 'and', 'free']
# for index,key in enumerate(a):
#     print(index,key)
#
# for letter in 'ityouknow':     # 第一个实例
#     if letter == 'n':        # 字母为 n 时跳过输出
#         continue
#     print(letter)

# def fib(n):
#     if n==2 or n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(20))

# class Car(object):
#     name = 'BMW'
#     def __init__(self, name):
#         self.name = name
#     def run(self,speed):
#         print('Car-->',self.name,speed,'行驶')
#
# c=Car('car')
# print(c.run('120mph'))
#
# dict = {'Name': 'Mary', 'Age': 17}
#
# print("Value : %s" % dict.items())
#
# table = {'Sjoerd': 123, 'Jack': 456, 'Dcab': 789789789789}
# print('Jack: {Jack}; Sjoerd: {Sjoerd}; Dcab: {Dcab}'.format(**table))
#
# with open('GL_050202_01.TXT', 'r+') as f:
#     str = f.readline()
#     # while True:
#     #
#     #     print(str,end='')
#     #     if len(str)==0:
#     #         break
#     for str in f:
#         print(str,end='')
#     f.close()

# name1='SuSan'
# if chr('SuSan'. __eq__(name1)):
#     result='I am from China'
# else:
#     result='I am from USA'
#
# print(result)

# def spam():
#     eggs = 99
#     eggs=bacon()
#     print(eggs)
# def bacon():
#     ham = 101
#     eggs = 0
#     return eggs
# spam()

# spam=['a', 'b', 'c', 'd']
# if spam[int('3' * 2) // 11]=='d':
#     print('you are right')
# else:
#     print('you should study harder')

# picnicItems = {'apples': 5, 'cups': 2}
# print('I am bringing ' + str(picnicItems.get('cakes')) + ' cakes.')
#
# spam = {'name': 'Zophie', 'age': 7,'color':'black'}
# print('black' in spam.values())


# # colWidths = [0] * len(tableData)
# # print(colWidths)

#

import os
# path1=os.getcwd()
# print(path1)
#
# print(str(path1).split('\\'))
# print(os.listdir(path1))


import webbrowser, requests
# # webbrowser.open('https://mp.weixin.qq.com/s?__biz=MzUyNTQ1NDQzMQ==&mid=2247484562&idx=2&sn=c23e991fa0c9cbcb821846cbde6f88e9&chksm=fa1c99a2cd6b10b4dffa727fa1d97b286e679043b10dd763d411670546829a7ce06d628bfa9e&mpshare=1&scene=1&srcid=&sharer_sharetime=1569720071850&sharer_shareid=9fffc7fa0a5ad851b324126500370832#rd')
# res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
# print(type(res))
# res.raise_for_status()
# print(res.text[:260])
# f=open('downfile.txt', 'wb')
# for chunk in res.iter_content(100000):
#     f.write(chunk)
# f.close()

# import bs4
#
# with open('example.html', 'w')as f:
#     f.write('''
#     <!-- This is the example.html example file. -->
# <html><head><title>The Website Title</title></head>
# <body>
# <p>Download my <strong>Python</strong> book from <a href="http://
# inventwithpython.com">my website</a>.</p>
# <p class="slogan">Learn Python the easy way!</p>
# <p>By <span id="author">Al Sweigart</span></p>
# </body></html>
#     ''')
# f=open('example.html')
# print(f)
# fsoup=bs4.BeautifulSoup(f.read())
# elems=fsoup.select('#author')
# print(elems[0].getText())
# print(elems[0].attrs)

'''
from selenium import webdriver
browser=webdriver.Edge("C:\\Users\\Basanwei\\AppData\\Local\\Programs\\Python\\Python37\\msedgedriver.exe")
browser.maximize_window()
browser.get('http://hotmail.com')'''

import requests
res=requests.get('https://mp.weixin.qq.com/s/SyC_LLQL8AU3i6wYNlOdNQ')
res.raise_for_status()
with open('../pyquestions.html', 'wb') as f:
    for chunk in res.iter_content(100000):
        f.write(chunk)