# -*- coding:utf-8 -*-
import os
os.getcwd()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# pd.set_option('display.max_rows',10) #this function doesn't work, why?

# df=pd.read_csv('GL_050202_01.csv',header=None,index_col=False,names=['Wavenumber','Intensity']) #this is the Raman spectrum of my sample
# print(df.head())
# print(df.describe())

# df_np=np.array(df)
# print(df_np[:,1])


# print(type(df))
# print(type(df.iloc[:,1]))   #df.iloc[:,1]=df.W=df.['I']=df.I
# print(df.iloc[:,1])
# print(df.Intensity)


# newserie=df.Intensity[:]/max(df.Intensity)
# # print(newserie)
# df['Normalized_Intensity']=newserie
# print(df)

# x=df.iloc[:,0]
# y=df.iloc[:,-1]
# plt.xlabel('Wavelength(nm)')
# plt.ylabel('Intensity(a.u.)')
# plt.title('Raman spectrum of Zinc Oxide')
# plt.plot(x,y)
# plt.show()

import random
import math

def randwalk(n):
    '''
    The function is to imitate random walk, which starts from the zero point(0,0)
    :param n: number of steps
    :return: the coordinates of endpoint of one-time walk with n steps
    '''
    x=0
    y=0
    for i in range(n):
        step=random.choice(['E','W','N','S'])
        if step=='E' :
            x+=1
        elif step=='W':
            x-=1
        elif step=='N':
            y+=1
        else:
            y-=1
    return(x,y)

farstep=0
nearstep=0
k=100
dslist = []
for j in range(k):
    d = randwalk(50)
    ds = math.sqrt(float(d[0]) ** 2 + float(d[1]) ** 2)

    if ds>=10:
        farstep+=1
    else:
        nearstep+=1
    dslist.append(ds)

print(dslist)
print(nearstep,farstep)

