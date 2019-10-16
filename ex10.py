# -*- coding:utf-8 -*-
import os
os.getcwd()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows',10) #this function doesn't work, why?

df=pd.read_csv('GL_050202_01.csv',header=None,index_col=False,names=['Wavenumber','Intensity']) #this is the Raman spectrum of my sample
print(df.head())
print(df.describe())

df_np=np.array(df)
print(df_np[:,1])


print(type(df))
print(type(df.iloc[:,1]))   #df.iloc[:,1]=df.W=df.['I']=df.I
print(df.iloc[:,1])
print(df.Intensity)


newserie=df.Intensity[:]/max(df.Intensity)
# print(newserie)
df['Normalized_Intensity']=newserie
print(df)

x=df.iloc[:,0]
y=df.iloc[:,-1]
plt.xlabel('Wavelength(nm)')
plt.ylabel('Intensity(a.u.)')
plt.title('Raman spectrum of Zinc Oxide')
plt.plot(x,y)
plt.show()

import random
import math
from ex6 import segment

# def randwalk(steps,times):
#     '''
#     The function is to imitate random walk, which starts from the zero point(0,0)
#     :param steps: number of steps
#     :param times: the number of times for walk
#     :return: the coordinates(x,y) of endpoint of one-time walk with n steps;the distance of one walk;
#     '''
#     x,y=0,0
#     farstep = 0
#     nearstep = 0
#     dslist = []
#     for j in range(times):
#         for i in range(steps):
#             direc=random.choice(['E','W','N','S'])
#             if direc=='E' :
#                 x+=1
#             elif direc=='W':
#                 x-=1
#             elif direc=='N':
#                 y+=1
#             else:
#                 y-=1
#         d=(x,y)
#         # print(d)
#
#         ds = round(math.sqrt(float(d[0]) ** 2 + float(d[1]) ** 2),2)
#         if ds>31:
#             farstep+=1
#         else:
#             nearstep+=1
#         dslist.append(ds)
#
#     print('The average distance for {} walk is {}'.format(times,sum(dslist)/times))
#     print(segment(dslist,10))
#     print(nearstep,farstep)
# randwalk(100,50)

