# -*- coding:utf-8 -*-
#Created on 2019年9月29日

#author: Basanwei

# print("adding numbers for maths practices")
# a=325+138
# print(a)
# print("power function for maths practices")
# b=12**3.1
# print(b)

# print("\"Yes,\" he said.")
# 
# print('please tell me your \name')
# print(r'please tell me your \name')
# 
# print(5*'I love you! '+ 'python')

# phrase='time is flying'
# print(phrase[5])
# print(phrase[5]+phrase[-2])
# print(phrase[1:7])
# print(len(phrase))

# sentence=['Casefolded', 'strings', 'may', 'be', 'used', 'for', 'caseless', 'matching']
# print(len(sentence))
# sentence[2:5]=['can','not','take']
# print(sentence)
# sentence[2]=[]
# print(sentence)

# Fibonacci series:
a, b = 0, 1
c=[]
while b<=500000000000:
      c.append(b)
      a, b = b, a+b
print(len(c),c)
#       
# a, b = 1, 2
# while b<=1000:
#       print(b, end=',')
#       a, b = b, b*2
# print()
       
# a, b = 1, 2
# for i in range(1,32):
#       print(b, end=',')
#       a, b = b, b*2      

# b = 1
# for i in range(1,32):
#       print(b, end=',')
#       b = b*2      
#       if b>10000:
#          break
# print()
# print('we only need these numbers!') 

# b = 1
# while b<10000:
#       print(b, end=',')
#       b = b*2      
#       
# print()
# print('we only need these numbers!')
class User:

    def __init__(self,full_name,birthday):

        self.name = full_name

        self.birthday = birthday



        name_splits = full_name.split(" ")

        self.first_name = name_splits[0]

        self.last_name = name_splits[-1]

GL=User("Guangqiang Lu",19780419)
print(GL.first_name)
print(GL.last_name)
print(GL.birthday)

# -*- coding: UTF-8 -*-

a = [1, 2, 3]
b = a
print(b)