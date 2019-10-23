# -*- coding:utf8 -*-
'''
The following are the answers to the questioned listed in book001.
'''
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
Question 4.10.2
'''
# for i in range(6):
#
#     for j in range(8):
#         picture=input()
#         if picture=='':
#             break
#         else:
#             print(picture,end='')
#     print()

