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