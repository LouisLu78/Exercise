# -*- coding:utf-8 -*-

import random
import math
import time
# from ex6 import segment
import matplotlib.pyplot as plt
start_time=time.time()
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

        d=(x,y)
        # print(d)


        ds = round(math.sqrt(float(x) ** 2 + float(y) ** 2), 2) # equivalent with 'ds = round(math.sqrt(float(d[0]) ** 2 + float(d[1]) ** 2),2)'
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
randwalk(50,1000)
randwalk(50,1000,dsavg)
end_time=time.time()
process_time=end_time-start_time
print('It takes {}s to finish this process.'.format(process_time))

# def dice():
#     num=random.randint(1,100)
#     if num<51:
#         luck=False
#     else:
#         luck=True
#     return luck
# Good,Bad=0,0
# for i in range(1000):
#     if dice():
#         Good+=1
#     else:
#         Bad+=1
# print('The times for good luck is ',Good)
# print('The times for bad luck is ',Bad)

# def gamble(funds,wager,times):
#     counts=1
#     global x, y
#     x=[]
#     y=[]
#     while counts<=times:
#         if dice():
#             funds+=wager
#
#         else:
#             funds-=wager
#         x.append(counts)
#         y.append(funds)
#         counts+=1
#     # print(segment(x,25),segment(y,25))
#     return x,y
#
# gamble(100,10,200)
#
# plt.xlabel('Wager times')
# plt.ylabel('Money left')
# plt.title('Simulation of gambling')
# plt.plot(x,y)
# plt.show()

# def gamble_varied(funds,wager,times):
#     counts=1
#     x = []
#     y = []
#     bet=wager
#     while counts <= times:
#         if dice():
#             funds+=bet
#             bet=wager
#         else:
#             funds-=bet
#             bet=bet*2
#         x.append(counts)
#         y.append(funds)
#         counts+=1
#         if funds<=0:
#             break
#     # print(segment(x,25),segment(y,25))
#     plt.plot(x, y)
#     return x, y
#
#
# for i in range(10):
#     gamble_varied(10000, 1000, 1000)


plt.xlabel('Wager times')
plt.ylabel('Money left')
plt.title('Simulation of gambling')
plt.show()