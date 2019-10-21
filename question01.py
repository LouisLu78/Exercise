# -*- coding:utf-8 -*-
'''
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''
# num=[]
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if k!=j and k!=i and j!=i:
#                 num.append(i*100+j*10+k)
# print(len(num),num)

'''
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？
'''
# I=int(input("Please input the interests of your company:"))
# stage=[100,60,40,20,10,0]
# rate=[0.01,0.015,0.03,0.05,0.075,0.1]
# Bonus=0
# for i in range(6):
#     if I>stage[i]:
#     Bonus+=(I-stage[i])*rate[i]
#     I=stage[i]
# print(Bonus)

# '''
# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# 程序分析：
# 假设该数为 x。
# 1、则：x + 100 = n2, x + 100 + 168 = m2
# 2、计算等式：m2 - n2 = (m + n)(m - n) = 168
# 3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数
# 4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
# 5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
# 6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。
# 7、接下来将 i 的所有数字循环计算即可。
# '''
# for i in range(2,85,2):
#     if 168%i==0:
#         j=168/i
#         if j%2==0 and i<j:
#             n=(i-j)/2
#             x=n**2-100
#             print(x)



# '''
# 输入某年某月某日，判断这一天是这一年的第几天？
# '''
# def leapyear(y):
#
#     if y%100==0:
#        if y%400==0:
#            judge=True
#        else:
#            judge=False
#     elif y%4==0:
#         judge = True
#     else:
#         judge=False
#     return judge
#
# date=int(input("please input a day with the format as YYYYMMDD:"))
# year=date//10000
# month=(date-year*10000)//100
# day=date-year*10000-month*100
# print(year,month,day)
#
# d=[31,28,31,30,31,30,31,31,30,31,30,31]
# added_day=day
# for i in range(12):
#     if month==i+1:
#         added_day+=sum(d[0:i])
#
# if leapyear(year) and month>2:
#     added_day+=1
#
# print('This day {} is the {}th day of the year.'.format(date,added_day))

# '''
# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
#
# 程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
# '''
# lst=[]
# for i in range(3):
#     x=int(input('please input an integer: '))
#     lst.append(x)
# lst.sort()
# print(lst)
# lst.reverse()
# print(lst)

# '''
# 题目：输出 9*9 乘法口诀表。
# 程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
# '''
import time
# for i in range(1,10):
#     print()
#     time.sleep(1)
#     for j in range(1,i+1):
#         print('{0:1d}*{1:1d}={2:2d}'.format(j,i,j*i), end=' ')

# '''
# 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
#
# 程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
# '''
# a,b=0,1
# while b<1000:
#     print(b, end=',')
#     a,b=b,a+b
#
'''
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
'''

# N=int(input("please input an natural number: "))
# from ex6 import seek_prinum
# import math
# num=N
# factors=[]
# pm=seek_prinum(N)
# counts=0
# while counts<len(pm):
#     if num in pm:
#         factors.append(num)
#         break
#     else:
#         for pmnumber in pm:
#             if num%pmnumber==0:
#                 factors.append(pmnumber)
#                 num=int(num/pmnumber)
#                 break
#     counts+=1
# print('{}='.format(N), end='')
# for i in range(len(factors)-1):
#     print('{}*'.format(factors[i]), end='')
# print(factors[-1])
#
#
# import datetime
# print(datetime.date.today().strftime('%Y/%m/%d'))
# # This function is to find today's date.
#
# '''
# Q18: 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
# 程序分析：关键是计算出每一项的值。
# '''
# '''suppose we have N terms'''
# def term(n):
#     Sum=0
#     for i in range(int(n)):
#         Sum+=10**i
#     # print(Sum)
#     return Sum
#
# S=0
# N=int(input('please give the value of N:'))
# a=int(input('please give the value of a:'))
# for i in range(1,N+1):
#     S+=term(i)
# S*=a
# print('The final result for the polynomial is:',S)
'''
Q19:一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
'''

start_time=time.time()
def find_factor(n):
    fac={1}
    if n==1 or n==2:
        fac.add(n)
    else:
        for i in range(2,n):
            if n%i==0:
                # fac.add(i),fac.add(int(n/i))
                fac.update({i, int(n/i)})
    return fac
print(find_factor(120))

perfect_num=[]
for i in range(1,1001):
    sumlist=list(find_factor(i))
    # print(sumlist)
    if i==sum(sumlist[:]):
        perfect_num.append(i)

print(perfect_num)
end_time=time.time()
process_time=end_time-start_time
print('It takes {}s to finish this process'.format(process_time))
















