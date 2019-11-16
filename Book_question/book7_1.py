'''
The following programs are the answers to the questions in book <A Primer on Scientific Programming with Python
Third Edition> by Hans Petter Langtangen. I wrote all the codes myself.
'''

#Question 1.6
def interests(p, n):
    '''
    :param p: interest rate a bank is offered.
    :param n: years
    :return:  the total amount of money when the deposit is drawn.
    '''
    sum=(1+p/100)**n
    return sum
A=1000
A*=interests(5, 5)
print('If you save 1000 in the bank, after 5 years you may get %.2f back.'%A )

#Question 1.10
from math import sqrt, exp, pi

def Gaussian_func(m, s, x):
    p=1/((sqrt(2*pi))*s)
    i=((x-m)/s)**2
    return p*exp(-0.5*i)
m, s, x = 0, 2, 1
print('The result for the Gaussian function is %.6f' % Gaussian_func(m, s, x))

