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
def Gaussian_func(m, s, x):

    from math import sqrt, exp, pi

    p=1/((sqrt(2*pi))*s)
    i=((x-m)/s)**2
    return p*exp(-0.5*i)
m, s, x = 0, 2, 1
print('The result for the Gaussian function is %.6f' % Gaussian_func(m, s, x))

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
    print(term)'''

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

'''
Exercise 3.11. Approximate π.
The value of π equals the circumference of a circle with radius 1/2.Suppose we approximate the circumference by a polygon through N +1
points on the circle. The length of this polygon can be found using the pathlength function from Exercise 3.10. Compute N + 1 points (xi, yi)
along a circle with radius 1/2 according to the formulas xi =1/2cos(2πi/N), yi = 1/2sin(2πi/N), i = 0, . . . , N.
Call the pathlength function and write out the error in the approximation of π for N = 2**k, k = 2, 3, . . . , 10. 
'''
list_N=[2**k for k in range(2,11)]
for N in list_N:
    x=[0.5*cos(2*pi*i/N) for i in range(N+1)]
    y=[0.5*sin(2*pi*i/N) for i in range(N+1)]
    print('Pi is approximately equavalent to {}, when N is {} '.format(pathlength(x,y), N))

