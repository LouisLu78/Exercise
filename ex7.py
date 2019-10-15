# -*- coding:utf-8 -*-
import os
# os.getcwd()
dir(os)

# print(sum(range(100)))

# with open('C:/Users/Basanwei/eclipse-workspace/try.txt', 'r+') as f:
#     for line1 in f:
#         print(line1, end='')
    # while True:
    #     line = f.readline()
    # #Zero length means End Of File
    #     if len(line) == 0:
    #         break
    #     print(line)

# y=int(input('please input a year number:'))
# if y%100==0:
#    if y%400==0:
#        print(y,' is a leap year')
#    else:
#        print(y, ' is not a leap year')
# elif y%4==0:
#     print(y, ' is a leap year')
# else:
#     print(y, ' is not a leap year')
    
import matplotlib.pyplot as plt
Month=range(1,13)

# y=[6,8,9,10,5,7,9,7,11,10,6,5]
# y1=[7,9,10,11,6,8,10,8,12,11,7,6]
# plt.xlabel('Month')
# plt.ylabel('Bonus')
# plt.title('Bonus of whole year\nbonus of Lufy')
# # plt.plot(Month,y)
# # plt.plot(Month,y1)
# plt.plot(Month,y,Month,y1)
# plt.scatter(Month,y,label='Sauron')
# plt.scatter(Month,y1,label='Lufy')
# plt.legend()
# plt.show()

City_C_Age=[2,3,1,7,4,5,3,1,7,6,9,8,13,16,12,17,15,14,18,20,23,28,25,23,27,25,29,26,24,25,30,34,37,36,38,32,35,37,36,41,42,47,47,48,43,46,44,53,54,58,52,51,55,56,69,60,63,67,64,72,74,78,75,89,85,83,90,93]
bins=range(0,100,10)
plt.xlabel('Age')
plt.ylabel('Number')
plt.title('Age distribution of City C')
plt.hist(City_C_Age,bins,histtype='bar',rwidth=0.8,color='red')
# plt.legend()
plt.show()

x=[1,2,3,4,5,6,7,8,9,10,11,12]
x1=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[6,8,9,10,5,7,9,7,11,10,6,5]
y1=[7,9,10,11,6,8,10,8,12,11,7,6]
plt.xlabel('Month')
plt.ylabel('Bonus')
plt.title('Bonus of whole year\nbonus of Lufy')
plt.scatter(x,y,label='Sauron',color='red',marker='*')
plt.scatter(x1,y1,label='Lufy',color='green',marker='.')
plt.legend()
plt.show()

# Month=range(1,13)
# A=range(1,13)
# B=range(10,130,10)
# C=range(220,100,-10)
# D=[80,90,86,88,82,84,90,87,83,81,85,88]
# plt.xlabel('Month')
# plt.ylabel('Sales')
# plt.title('A, B, C, D, Sales')
#
# plt.plot([],[],color="m",label="Company A",linewidth=8)
# plt.plot([],[],color="r",label="Company B",linewidth=8)
# plt.plot([],[],color="k",label="Company C",linewidth=8)
# plt.plot([],[],color="c",label="Company D",linewidth=8)
#
# plt.stackplot(Month,A,B,C,D,colors=["m","r","k","c"])
# plt.legend()
# plt.show()

# Nation=['China','USA','Japan','India']
# GDP=[13.1,20.7,4.9,2.7]
# cmcolor=['azure','lavender','pink','red']
# plt.title('GDP of main countries in 2018')
# plt.pie(GDP,
#          labels=Nation,
#          colors=cmcolor,
#          startangle=60,
#          shadow=True,
#          autopct='%1.2f%%',
#          explode=(0.1,0,0,0)
#         )
#
# plt.show()

# Nation=['China','USA','Japan','India']
# GDP=[13.1,20.7,4.9,2.7]
# # cmcolor=['azure','lavender','pink','red']
# plt.title('GDP of main countries in 2018')
# plt.xlabel('Nation')
# plt.ylabel('GDP / trillion USD')
# plt.bar(Nation,GDP)
# plt.legend()
# plt.show()


