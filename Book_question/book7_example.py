# -*- coging: utf-8 -*-
# author: Guangqiang Lu time:2019:11:20

import matplotlib.pyplot as plt
import numpy as np
'''This is example 1.

t =np.linspace(0, 3, 51)
y1=t**2*np.exp(-t**2)
y2=t**2*y1
plt.plot(t, y1)
# plt.hold('on')
plt.plot(t, y2)
plt.xlabel('t')
plt.ylabel('y')
plt.legend('y1', 'y2')
plt.title('Plotting two curves in the same plot')
plt.savefig('tmp3.png')
plt.show()



def f(x, m, s):
    return (1.0/(np.sqrt(2*np.pi)*s))*np.exp(-0.5*((x-m)/s)**2)

plt.ion()
m = 0
s_min = 0.2
s_max = 2
x = np.linspace(m -3*s_max, m + 3*s_max, 1000)
s_values = np.linspace(s_max, s_min, 30)
max_f = f(m, m, s_min)

y = f(x, m, s_max)
lines =plt.plot(x, y)
plt.axis([x[0], x[-1], -0.1, max_f])
plt.xlabel('x')
plt.ylabel('f')
counter = 0
for s in s_values:
    y = f(x, m, s)
    lines[0].set_ydata(y)
    plt.draw()
    plt.legend(['s=%4.2f' % s])
    plt.savefig('tmp_%04d.png' % counter)
    counter += 1'''

content='''air 0.0012
gasoline 0.67
ice 0.9
pure water 1.0
seawater 1.025
human body 1.03
limestone 2.6
granite 2.7
iron 7.8
silver 10.5
mercury 13.6
gold 18.9
platinium 21.4
Earth mean 5.52
Earth core 13
Moon 3.3
Sun mean 1.4
Sun core 160
proton 2.8E+14
with open('test.txt', 'w') as f:
    f.write(content)
infile=open('test.txt', 'r')
print(infile.readline())
f1=infile.readlines()
for line in f1:
    print (line)'''
import sys
sys.path.append(r'D:\Program files\JetBrains\my_module')



from math import sin, pi
from integral import Integral
from derivative import derivative

G = Integral(sin, 0, n=100)
result = G(0.5*pi)
print(result)

res=derivative(sin, pi/3)
print(res)











