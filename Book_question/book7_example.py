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
plt.show()'''



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
    counter += 1

