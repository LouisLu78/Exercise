# -*- coding:utf-8 -*-

import random
import math
from ex6 import segment

def randwalk(steps,times,estimated_ds=10):
    '''
    The function is to imitate random walk, which starts from the zero point(0,0)
    :param steps: number of steps
    :param times: the number of times for walk
    :param estimated_ds: estimated distance for one walk
    :return: the coordinates(x,y) of endpoint of one-time walk within n steps;the distance of one walk;
    '''

    x,y=0,0
    farstep = 0
    nearstep = 0
    dslist = []
    for j in range(times):
        for i in range(steps):
            (dx,dy)=random.choice([(1,0),(-1,0),(0,1),(0,-1)])
            x+=dx
            y+=dy

        d=[x,y]
        # print(d)

        ds = round(math.sqrt(float(d[0]) ** 2 + float(d[1]) ** 2),2)
        if ds>estimated_ds:
            farstep+=1
        else:
            nearstep+=1
        dslist.append(ds)

    print('The average distance for {} walk is {}'.format(times,sum(dslist)/times))
    # print(segment(dslist,10))
    print(nearstep,farstep)

    global dsavg
    dsavg =sum(dslist)/times
randwalk(1000,5000)
randwalk(1000,5000,dsavg)

