# -*- coding:utf-8 -*-
'''
Created on 2019��9��30��

@author: Basanwei
'''
words = ['cat', 'window', 'defenestrate','carelessness']
for w in words:
    if len(w)>6:
        words.insert(0, w)
        print(words)


# for num in range(2, 10):
#     if num % 2 == 0:
#         print("Found an even number", num)
#         break
#     print("Found a even number", num)

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        
    else:
         print("Found a odd number", num)
    continue