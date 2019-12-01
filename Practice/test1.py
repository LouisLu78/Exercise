# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/11/30
# If not explicitly pointed out, all the codes are written by myself.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# fig, ax=plt.subplots()
# xdata, ydata=[],[]
# ln,=ax.plot([],[],'b-',animated=False)
# def init():
#     ax.set_xlim(0, 3)
#     ax.set_ylim(0, 0.6)
#     return ln,
#
# def update(frame):
#     xdata.append(frame)
#     ydata.append(frame**2*np.exp(-frame**2))
#     ln.set_data(xdata, ydata)
#     return ln,
#
# ani = FuncAnimation(fig, update, frames=np.linspace(0, 3, 100),
#                     init_func=init, blit=True)
# plt.show()


fig, ax=plt.subplots()
xdata, y1data, y2data=[], [], []
ln,=ax.plot([],[],'b-',animated=False)
line,=ax.plot([],[],'r-',animated=False)
def init():
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 0.6)
    return ln, line,

def update(frame):
    xdata.append(frame)
    y1data.append(frame**2*np.exp(-frame**2))# two animated curves shown in one figure
    y2data.append(frame**4*np.exp(-frame**2))
    ln.set_data(xdata, y1data)
    line.set_data(xdata, y2data)
    return ln,line,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 3, 50),
                    init_func=init, blit=True)
plt.show()