# -*- coding:utf8 -*-
# this is question3.11.1
def collatz(num):
    if num%2==0:
        result=num//2
    else:
        result=num*3+1
    print(result)
    return result

number=int(input('Please input a natural number:'))
s=collatz(number)
final=[s]
while s!=1:
    s=collatz(s)
    final.append(s)
print(len(final),final)
