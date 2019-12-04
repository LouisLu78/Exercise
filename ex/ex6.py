# -*- coding: utf-8 -*-
'''
Created on 2019��10��11��

@author: Basanwei
'''
from _collections_abc import Iterator
isinstance([1,2,3],Iterator)



# f=open('C:/Users/Basanwei/eclipse-workspace/try.txt', 'w+')
# str=''' search for all the primary numbers within n
#     
#     
#     INPUT:
#     n: the upper limit of the number, within which all the primary
#     number is sought.
#     OUTPUT:
#     a list of all the primary number within n'''
# f.write(str)
# f.close()
# with open('C:/Users/Basanwei/eclipse-workspace/try.txt', 'r+') as f:
#     for line in f:
#         print(line, end='')
# f.close()

# from math import factorial
# print(factorial(10))


def seek_prinum(n):
    '''
    search for all the primary numbers within n


    INPUT:
    n: the upper limit of the number, within which all the primary
    number is sought. n is a natural number.
    OUTPUT:
    a list of all the primary number within n
    '''


    if n==1:
        pm=[]
    elif n==2:
        pm=[n]
    else:
        pm = [2]
        for k in range(3, n + 1):
            for i in range(2, k):
                if k % i == 0:
                    break
            else:
                pm.append(k)
    print(len(pm), pm)
    return pm
# seek_prinum(500)

# def segment(iterables, size):
#     '''
#     cut a long list or dictionary into small pieces.
#
#     :param iterables: a list or dictionary
#     :param size: length of the small list
#     :return: lists with predetermined length/size
#     '''
#     # newlist=[]
#     # for i in range(0,len(iterables),size):
#     #
#     #     newlist.append(list(iterables[i:i+size]))
#     newlist=[iterables[i:i+size] for i in range(0,len(iterables),size)]
#     for smalllist in newlist:
#         print(smalllist)
#     return
# list1=seek_prinum(5000)
#
# segment(list1, 10)
# segment(list1, 25)
