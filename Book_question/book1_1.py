# -*- coding:utf8 -*-
'''
The following are the answers to the questioned listed in book001.
'''
import re
# this is question3.11.1
# def collatz(num):
#     if num%2==0:
#         result=num//2
#     else:
#         result=num*3+1
#     print(result)
#     return result
# try:
#     number=int(input('Please input a natural number:'))
#     s=collatz(number)
#     final=[s]
#     while s!=1:
#         s=collatz(s)
#         final.append(s)
#     print(len(final),final)
#
# except ValueError:
#     print('You should input a number instead of a string.')

'''
Question:4.10.1
'''
# def change(list):
#     str1=''
#     for i in range(len(list)-1):
#         str1=str1+str(list[i])+','
#     str1=str1+'and'+str(list[-1])
#     return str1
# spam=[3.14, 'cat', 11, 'cat', True]
# print(change(spam))
# spam1 = [1, 3, 2, 4, 'Alice', 'Bob']
# print(change(spam1))

'''
This is question 6.7
'''

# tableData = [['apples', 'oranges', 'cherries', 'banana'],
# ['Alice', 'Bob', 'Carol', 'David'],['dogs', 'cats', 'moose', 'goose']]
#
# def maxlength(lis):      #find the value of maximum length in the strings of a given list.
#     a=max(list(len(lis[j]) for j in range(len(lis))))
#     return a
#
# def printtable(tdata):
#     width=max(maxlength(tdata[i]) for i in range(len(tdata)))
#     for i in tdata:
#         print(i[0].rjust(width),end=' ')
#         for j in range(1,len(i)):
#             print(i[j].ljust(width+1),end='')
#         print()
#
# printtable(tableData)

'''
This is question8.9.2
'''

# with open('replacetext.txt', 'w') as f:
#     f.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')
#
# f=open('replacetext.txt', 'r')
# message=f.read()
# f.close()
# print(message)
#
# Nounre=re.compile(r'Noun',re.I)
# Adjre=re.compile(r'Adjective',re.I)
# Verbre=re.compile(r'Verb',re.I)
#
# text=Nounre.sub('chandelier', message,1)
# text=Nounre.sub('pickup truck', text)
# text=Adjre.sub('silly', text)
# text=Verbre.sub('screamed', text)
#
# print(text)
#
# with open('subtext.txt', 'w') as f:
#     f.write(text)
# f=open('subtext.txt', 'r')
# text=f.read()
# print(text)
# f.close()

'''
9.8.1编写一个程序， 遍历一个目录树，查找特定扩展名的文件（诸如.pdf 或.jpg）。不论这些文件的位置在哪里， 将它们拷贝到一个新的文件夹中。


import os, shutil
for folderName, subfolders, filenames  in os.walk('F:'):
    for filename in filenames:
        if filename.endswith('.pdf'):
            shutil.copy(os.path.join(folderName, filename), 'C:\\QMDownload')
            print(filename)
            '''
'''
7.18.1 强口令检测
写一个函数，它使用正则表达式， 确保传入的口令字符串是强口令。 强口令的定义是： 长度不少于 8 个字符， 同时包含大写和小写字符， 至少有一位数字。

def check_code(code):
    str(code)
    realphalower=re.compile(r'[a-z]')
    realphaupper = re.compile(r'[A-Z]')
    redig=re.compile(r'[0-9]')
    respace=re.compile(r'\s|\.')
    flag=True

    if len(code)<8:
        flag=False
    elif respace.search(code)!=None:
        flag=False
    elif realphalower.search(code) is None or realphaupper.search(code)is None or redig.search(code) is None:
        flag=False
    else:
        pass

    return flag
passcode=input('Please enter your password:')
if check_code(passcode):
    print('The given password is qualified. ')
else:
    print('Your password doesn\'t meet our requirement.')
    
'''
def is_valid_email(addr):
    Regex=re.compile(r'^[a-z]+(\.)*[a-z]+@[a-z]+\.com', re.I)
    Mo=Regex.search(addr)
    if Mo != None:
        return True
if is_valid_email('bob#example.com'):
    print('it\'s valid.')
else:
    print('it\'s not a valid email.')






