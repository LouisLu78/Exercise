# -*- coding:utf-8 -*-

'''
Created on 2019��10��10��

@author: Basanwei
'''
# names1=["tom","jimmy","william","john","mike"]
# Newname=iter(names1)
# print(next(Newname))
from pdb import pm

names=["William","Mary","Tommy","Jimmy"]
heights=[185,173,164,175]
alo=list(zip(names,heights))
print(alo)
# alo=zip(names,heights)
# print(list(alo))
# blo=zip(names,heights)
# print(dict(blo))

# number_list=[number**2 for number in range(1,7) if number%2==0]
# 
# print(number_list)

# number_list=[number*number 
# 
#                        if number%2==0
# 
#                        else number+8
# 
#                        for number in range(1,7)]
# 
# print(number_list)


# nlist=[]
# for i in range(1,7):
#     if i%2==0:
#         nlist.append(i**2)
#     else:
#         nlist.append(i+8)
# print(nlist)
#       
# nlist=[]
# i=1
# while i<7:
#     if i%2==0:
#         nlist.append(i**2)
#     else:
#         nlist.append(i+8)
#     i+=1    
# print(nlist)

# names=["William Wang","Jack Ma","Pony Ma","Jack Chen","Jet Li"]
#   
# first_name=[name.split()[0] for name in names]
#   
# last_name=[name.split()[-1] for name in names]
#   
# print(first_name)
#   
# print(last_name)
# 
# 
# vipname=["William Wang","Jack Ma","Pony Ma","Jack Chen","Jet Li"]
# firstname=[]
# lastname=[]
# for fullname in vipname:
#     firstname.append(fullname.split()[0])
#     lastname.append(fullname.split()[-1])
#   
# print(firstname) 
# print(lastname)


# names=["William Wang","Jack Ma","Pony Ma","Jack Chen","Jet Li"]
# 
# for i in range(len(names)):
#     print(names[i])

# def add_number(num1,num2,num3):
# 
#     result=num1/num2*num3
# 
#     print("so much fun")
# 
#     return result
# print(add_number(5,3,4))


# class MyClass:
#     """A simple example class"""
#     i = 12345
#     def f(self):
#         return print('hello world')

# def multi(pra1,pra2):
#     return print('the product is', pra1*pra2)
# multi(3,5)

# multi=lambda pra1,pra2:pra1*pra2
# print(multi(23,15.9))
    
def seek_prinum(n):
    '''
    search for all the primary numbers within n
    
    
    INPUT:
    n: the upper limit of the number, within which all the primary
    number is sought.
    OUTPUT:
    a list of all the primary number within n
    '''    
    
    pm=[2]

    for k in range(3,n+1):
        for i in range(2,k):
            if k%i==0:
               break
        else:
            pm.append(k) 
        
    return print(pm)


# seek_prinum(2)
       
print(seek_prinum.__doc__)
        
    
    
    
    
    
    