'''
The following programs are the answers to the questions in book <A Primer on Scientific Programming with Python
Third Edition> by Hans Petter Langtangen. I wrote all the codes myself.
'''

#Question 1.6
# def interests(p, n):
#     '''
#     :param p: interest rate a bank is offered.
#     :param n: years.
#     :return:  the total amount of money when the deposit is drawn.
#     '''
#     sum=(1+p/100)**n
#     return sum
# A=1000
# A*=interests(5, 5)
# print('If you save 1000 in the bank, after 5 years you may get %.2f back.'%A )
'''
#Question 1.10
from Gaussian_function import Gaussian_func

m, s, x = 0, 2, 1
print('The result for the Gaussian function is %.4f' % Gaussian_func(m, s, x))

# import  math
# print(help(math))
#Q2.5
n=100
odd_num=[num for num in range(n) if num%2==1]
print(odd_num)

#Q2.11
x_coordinate=[1+i*0.01 for i in range(100)]
print(x_coordinate)


Q.20
Rewrite the generation of the nested list q,
q = [r**2 for r in [10**i for i in range(5)]]

list_r=[]
q=[]
for i in range(5):
    list_r.append(10**i)
for r in list_r:
    q.append(r**2)
print(q)

#Q3.5
#Exercise 3.5. Integrate a function by one trapezoid.
def trapezint1(f, a, b):
    return (b-a)/2*(f(a)+f(b))

from math import exp, sin, cos, log, pi

res_f1=trapezint1(exp, 0, log(3))
res_f2=trapezint1(cos, 0, pi)
res_f3=trapezint1(sin, 0, pi)
for term in zip(['exp','cos','sin'], [res_f1,res_f2,res_f3]):
    print(term)

# Q3.10
# Compute the length of a path.
from math import sqrt, pi, cos, sin

def pathlength(x, y):

    sum=0
    for i in range(1, len(x)):
        sum+=sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1])**2)
    return sum

x, y= zip((1, 1), (2, 1), (1, 2), (1, 1))
print(x)
print(y)
print(pathlength(x,y))


Exercise 3.11. Approximate π.
The value of π equals the circumference of a circle with radius 1/2.Suppose we approximate the circumference by a polygon through N +1
points on the circle. The length of this polygon can be found using the pathlength function from Exercise 3.10. Compute N + 1 points (xi, yi)
along a circle with radius 1/2 according to the formulas xi =1/2cos(2πi/N), yi = 1/2sin(2πi/N), i = 0, . . . , N.
Call the pathlength function and write out the error in the approximation of π for N = 2**k, k = 2, 3, . . . , 10. 

list_N=[2**k for k in range(2,15)]
for N in list_N:
    x=[0.5*cos(2*pi*i/N) for i in range(N+1)]
    y=[0.5*sin(2*pi*i/N) for i in range(N+1)]
    print('Pi is approximately equivalent to %.8f, when N is %d. ' %(pathlength(x,y), N))
'''
'''
Exercise 3.20. Compute velocity and acceleration from position data;one dimension.
Let x(t) be the position of an object moving along the x axis. The velocity v(t) and acceleration a(t) can be approximately computed by
the formulas v(t) ≈ (x(t + Δt) − x(t − Δt))/2Δt , a(t) ≈ (x(t + Δt) − 2x(t) + x(t − Δt))/Δt**2,
where Δt is a small time interval. As Δt → 0, the above formulas approach the first and second derivative of x(t), which coincide with
the well-known definitions of velocity and acceleration.
Write a function kinematics(x, t, dt=1E-6) for computing x, v, and a time t, using the above formulas for v and a with Δt corresponding to
dt. Let the function return x, v, and a. Test the function with the position function x(t) = e−(t−4)2 and the time point t = 5 (use Δt = 10−5).

from math import exp


def x(t):
    return exp(-(t - 4) ** 2)

def kinematics(x, t, dt=1E-6):
    s=x(t)
    v= (x(t+dt)-x(t-dt))/(2*dt)
    a=(x(t+dt)-2*x(t)+x(t-dt))/dt**2

    return s, v, a
s,v,a=kinematics(x, 5, dt=1E-5)
print(s, v, a, sep='\n')'''

'''Q3.30
Make a table for approximations of cos x.

def C(n,x):
    def term(j, x):
        if j == 0:
            return 1
        else:
            return -term((j - 1), x) * x ** 2 / (2 * j * (2 * j - 1))

    return sum(term(j,x) for j in range(n+1))

from math import pi
for x in [4*pi, 6*pi, 8*pi, 10*pi]:
    print('x=%.4f'%x)
    for n in [5, 25, 50, 100, 200]:
        print('%12.2E' %C(n,x), end=' ')
    print()


Exercise 3.34. Find pairs of characters.
Write a function count_pairs(dna, pair) that returns the number of occurrences of a pair of 
characters (pair) in a DNA string (dna).

def count_pairs(dna, pair):
    count=0
    for i in range(0,len(dna)-1):
        if dna[i:i+2]==pair:
            count+=1
    return count

dna='ACTGCTATCCATAT'
pair="AT"
print(count_pairs(dna,pair))'''

'''Exercise 4.25.
1. What is the probability of getting two heads when flipping a coin five times?
This probability corresponds to n = 5 events, where the success of an event means getting head, which has probability p = 1/2, 
and we look for x = 2 successes.

from binomial_distribution import binomial

n,x,p=5,2,0.5
result=binomial(x,n,p)
print('The probability is',result)'''

'''
exercise 5.1,5.3,5.4

import numpy as np
import matplotlib.pyplot as plt
from Gaussian_function import Gaussian_func

def h(x):
    Gf=np.vectorize(Gaussian_func)
    return Gf(0,1,x)

x=np.linspace(-4,4,100)
y=h(x)
plt.xlabel('x')
plt.ylabel('h(x)')
plt.title('Plot of Gaussian function')
plt.plot(x,y)
plt.show()

'''#Exercise 5.14. Implement Lagrange’s interpolation formula.
'''
import numpy as np
def L_k(x, k, xp):

    product=1
    for i in np.arange(0,len(xp),1):
        if i!=k:
            product*=(x-xp[i])/(xp[k]-xp[i])
        else:
            continue
    return product

def p_L(x, xp, yp):

    sum=0
    for k in np.arange(0,len(xp),1):
        sum+=yp[k]*L_k(x, k, xp)

def _verify():

    xp=np.linspace(0,np.pi,5)
    yp=np.sin(xp)
    for k in range(len(xp)):
        eps=p_L(xp[k],xp,yp)-yp
        print(eps)

if __name__=='__main__':
    _verify()'''

'''
Exercise 5.17. Plot a wave packet.
The function (5.18) describes for a fixed value of t a wave localized in space. Make a program
that visualizes this function as a function of x on the interval [−4, 4] when t = 0. 

import numpy as np
import matplotlib.pyplot as plt

def f(x,t):
    from numpy import pi, exp, sin

    p=exp(-(x-3*t)**2)
    c=sin(3*pi*(x-t))
    return p*c

x=np.linspace(-4,4,100)
y=f(x,t=0)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of wave packet')
plt.plot(x,y)
plt.savefig('wave_packet_ex5.17.png')
plt.show()'''

'''
#Exercise 5.21. Plot Taylor polynomial approximations to sin x.

import numpy as np
import matplotlib.pyplot as plt


def term(x, j):
    from math import factorial
    return ((-1) ** j) * (x ** (2 * j + 1)) / factorial(2 * j + 1)

def S(x,n):
    result=sum(term(x,j) for j in range(n+1))
    return result

x=np.linspace(0, 2*np.pi, 100)
y=S(x, 10)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Plot of sine function')
plt.plot(x,y)
plt.savefig('sine_ex5.21.png')
plt.show()'''

'''
Exercise 5.34 Demonstrate energy concepts from physics.

import numpy as np
import matplotlib.pyplot as plt
def P(y):
    #The potential energy
    return m*g*y

def K(v):
    #the kinetic energy
    return 0.5*m*v**2
def v(t):
    return v0-g*t
m,g,v0=50,9.8,10
t=np.linspace(0, 2*v0/g, 100)
y=v0*t-0.5*g*t**2
v=v0-g*t
f1=P(y)
f2=K(v)
f3=f1+f2
plt.xlabel('time')
plt.ylabel('Energy')
plt.title('Plot of Energy of a moving object')
plt.plot(t,f1,t,f2,t,f3)
plt.legend(['potential','kinetic','total'])
plt.savefig('energy_ex5.34.1.png')
plt.show()'''

'''
Exercise 6.1&6.3. Read a two-column data file.

#method one
with open('xy.dat', 'r') as infile:
    lines=infile.readlines()
    x=[float(line.split()[0]) for line in lines]
    y=[float(line.split()[1]) for line in lines]
print(x,y)

#method two
import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt('xy.dat')
x,y=data[:,0],data[:,1]

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot by data reading from a file')
plt.scatter(x,y)
plt.plot(x,y,'r')
plt.savefig('ex6.1.png')
plt.show()'''

'''
Exercise 6.16. Compare data structures for polynomials
'''
p={0:0.5,100:2}
sum=0
x=1.05
for power,para in p.items():
    sum+=float(para)*x**float(power)
print(sum)




