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



'''
输入某年某月某日，判断这一天是这一年的第几天？
'''
def leapyear(y):
    judge=None
    if y%100==0:
       if y%400==0:
           judge=True
       else:
           judge=False
    elif y%4==0:
        judge = True
    else:
        judge=False
    return judge

date=int(input("please input a day with the format as YYYYMMDD:"))
year=date//10000
month=(date-year*10000)//100
day=date-year*10000-month*100
print(year,month,day)

d=[31,28,31,30,31,30,31,31,30,31,30,31]
added_day=day
for i in range(12):
    if month==i+1:
        added_day+=sum(d[0:i])

if leapyear(year)==True:
    added_day+=1

print('This day {} is the {}th day of the year.'.format(date,added_day))







