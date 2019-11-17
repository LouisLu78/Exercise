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

# start_time=time.time()
# def find_factor(n):
#     fac={1}
#     if n==1 or n==2:
#         fac.add(n)
#     else:
#         for i in range(2,n):
#             if n%i==0:
#                 # fac.add(i),fac.add(int(n/i))
#                 fac.update({i, int(n/i)})
#     return fac
# print(find_factor(120))
#
# perfect_num=[]
# for i in range(1,1001):
#     sumlist=list(find_factor(i))
#     # print(sumlist)
#     if i==sum(sumlist[:]):
#         perfect_num.append(i)
#
# print(perfect_num)
# end_time=time.time()
# process_time=end_time-start_time
# print('It takes {}s to finish this process'.format(process_time))

'''
Q20:题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''
# def bounce(n):
#     if n==0:
#         return 100
#     else:
#         return bounce(n-1)*0.5
# height=bounce(0)
# for i in range(1,10):
#     height+=2*bounce(i)
# print('After 10 times of falling down, the route is {} meters'.format(height))
# print('The height of the tenth rebouncing is {} meter'.format(bounce(10)))
#
# def bounce(n):
#     h=0
#     if n==0:
#         h=100
#     else:
#         h=bounce(n-1)*0.5
#     return h
# print(bounce.__name__)
'''
Q21:猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
'''
# def peach(k):
#     if k==0:
#         return 1
#     else:
#         return (peach(k-1)+1)*2
# print(peach(9))

'''
Q22:题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
'''
# Jia=['a','b','c']
# Yi=['x','y','z']
# contest=[]
# for J in Jia:
#     for Y in Yi:
#         contest.append([J,Y])
# contest.remove(['a','x'])
# contest.remove(['c','x'])
# contest.remove(['c','z'])
# for i in range(len(contest)):
#     print(contest[i])

'''
Q24有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

程序分析：请抓住分子与分母的变化规律。

'''
# def fib(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# sum=0
# for i in range(20):
#     sum+=fib(i+2)/fib(i+1)
# print('The sum of the first 20 terms is ',sum)

'''
Q25 题目：求1+2!+3!+...+20!的和
'''
# def facto(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*facto(n-1)
# sum1=0
# for i in range(1,21):
#     sum1+=facto(i)
# print('The sum is', sum1)

'''
Q28:有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？

程序分析：利用递归的方法，递归分为回推和递推两个阶段。要想知道第五个人岁数，需知道第四人的岁数，依次类推，推到第一人（10岁），再往回推。
'''
# def age(n):
#     if n==1 :
#         return 10
#     else:
#         return age(n-1)+2
# print('The age of the 5th person is', age(5))

'''
Q29 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''

# num=int(input('please enter a natural number less than 100000:'))
#
# digi=num
# for i in range (1,6):
#     if digi//10==0:
#         break
#     else:
#         digi=digi//10
# print('The number is a {}-digit number'.format(i))
#
# s=str(num)
# for j in range((len(s)-1),-1,-1):
#     print(s[j])

'''
Q30 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
'''
# num=input('Please give a five-digit natural number:')
# flag=True
# for i in range(5):
#     if num[i]!=num[4-i]:
#         flag=False
#         break
# if flag:
#     print('it is.')
# else:
#     print('it is not.')


'''
Q31 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
'''
# weekday=input('please enter the weekday:')
# weekday=weekday.upper()
# print(weekday)
#
# if weekday[0]=='M':
#     print('It\'s Monday.')
#
# elif weekday[0]=='T':
#     if weekday[1]=='U':
#         print('It\'s Tuesday.')
#     else:
#         print('It\'s Thursday.')
# elif weekday[0]=='S':
#     if weekday[1]=='U':
#         print('It\'s Sunday.')
#     else:
#         print('It\'s Saturday.')
# elif  weekday[0]=='W':
#     print('It\'s Wednesday.')
# else:
#     print('It\'s Friday.')

'''
Q38 求一个3*3矩阵主对角线元素之和。
'''
# import numpy as np
# matrix=np.arange(3,12).reshape(3,3)
# sum2=0
# print(matrix)
# for i in range(3):
#     for j in range(3):
#         if i==j or i+j==2:
#             sum2+=matrix[i,j]
# print(sum2)

'''
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。
'''
# def inser(lst,num):            #list: a given list; num: a number to be inserted
#     lst.sort()
#     for i in range(len(lst)):
#         if num<lst[i]:
#             lst.insert(i,num)
#             break
#         elif num>lst[-1]:
#             lst.append(num)
#             break
#         else:
#             pass
#     print(lst)
#
# lista=[5,3.14,28,1]
# inser(lista,6)

'''
Q44 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
'''
# import numpy as np
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
#
# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]
#
#
# matX=np.array(X)
# maty=np.array(Y)
# sum=np.add(matX,maty)
# print(sum)
#
# import matplotlib.pyplot as plt
#
#
# x=np.linspace(-1.0,1.0,num=500)
#
# y1 = np.sqrt(1-x*x)
# y2 = -np.sqrt(1-x*x)
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('This is a circle with radius of one')
# plt.plot(x,y1,x,y2)
# plt.show()
#
# t=np.linspace(-np.pi, np.pi, num=500)
# x=np.cos(t)
# y=np.sin(t)
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('This is a true image of circle with radius of one')
# plt.plot(x,y)
# plt.show()

'''
有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数
'''
# def migration(list, m):
#     n=len(list)
#     list_end=list[n-1]
#     for i in range(n-1,-1,-1):
#         list[i]=list[i-1]
#     list[0]=list_end
#     m-=1
#     while m>0:
#         migration(list, m)
#     return list
# list_b=[5,3,28,1]
# migration(list_b, 2)
# print(list_b)

'''
有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
'''
def count(n):
    i,m,k=0,0,0
    num=list(range(1,n+1))
    while m < n - 1:

        if num[i] != 0:
            k += 1
        if k == 3:
            num[i] = 0
            k = 0
            m += 1
        i += 1
        if i == n:
            i = 0

    i = 0
    while num[i] == 0:
        i += 1
    print(num[i])

count(34)

a=[3,6,4,8,17] #Q73
print(a[::-1])

'''
Q76 :编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
'''
# def add(n):
#     summ=0
#     while n>0:
#         summ+=1/n
#         n=n-2
#     return summ
#
# def add_alt(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 0.5
#     else:
#         return 1/n+add_alt(n-2)
#
# print(add(5))
# print(add(4))
# print(add_alt(5))
# print(add_alt(4))

'''
Q80:题目：海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。
第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，
问海滩上原来最少有多少个桃子？
'''

# count=0
# while True:
#     left=count
#     for i in range(5):
#         left=(left*5-1)/4
#         if left%1!=0 or (left-1)/5<=0:
#             break
#
#     count+=1
#     if  i==4 and left%1==0:
#         print(int(left))
#         break
'''
Q89 某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,
然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
'''

num=input('please input a 4-digit number:')
c=list(int(i) for i in num)
sum=0

for i in range(4):
    c[i]+=5
    c[i]=c[i]%10

c[0],c[3]=c[3],c[0]
c[1],c[2]=c[2],c[1]

for i in range(4):
    sum+=c[3-i]*10**i
print(sum)












