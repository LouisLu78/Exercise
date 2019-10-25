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
This is question 6.7
'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],['dogs', 'cats', 'moose', 'goose']]

def maxlength(lis):      #find the value of maximum length in the strings of a given list.
    a=max(list(len(lis[j]) for j in range(len(lis))))
    return a

def printtable(tdata):
    colWidths=list(maxlength(tdata[i]) for i in range(len(tdata)))
    width=max(colWidths)
    for i in tdata:
        print(i[0].rjust(width),end=' ')
        for j in range(1,len(i)):
            print(i[j].ljust(width+1),end='')
        print()

printtable(tableData)
