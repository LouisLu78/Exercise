# -*- coding:utf-8 -*-
'''
Created on 2019��10��9��

@author: Basanwei
'''
# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
# a=Complex(2, 5)
# print(a.r, a.i)

# a=list(range(0,30,5))
# 
# print(a)

names1=["tom","jimmy","william","john","mike"]
names=[]
for index in range(len(names1)):
 
#     names.insert(index,names1[index].title())
    names.append(names1[index].title())
 
print(names)
# 
# names1=["tom","jimmy","william","john","mike"]
# 
# for index in range(len(names1)):
# 
# #     names.insert(index,names1[index].title())
#     names1[index]=names1[index].title()
# 
# print(names1)

# names={"Tom Zhao":"He is very cute.","Jimmy Qian":"He is very rich.","William Sun":"He is a little bit shy.","John Li":"He is very handsome."}
# 
# for a in names:
# 
#     print(a)

names={"Tom Zhao":"He is very cute.","Jimmy Qian":"He is very rich.","William Sun":"He is a little bit shy.","John Li":"He is very handsome."}
  
for key,value in names.items():
  
    print("Name:,{0}, Saying:,{1}".format(key,value))



# names={"Tom Zhao":"He is very cute.","Jimmy Qian":"He is very rich.","William Sun":"He is a little bit shy.","John Li":"He is very handsome."}
# 
# for key,value in names.items():
# 
#     print("Name:{}    Saying:{}".format(key,value))
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
# for name, phone in table.items():
#     print('{0:10} ==> {1:10d}'.format(name, phone))








