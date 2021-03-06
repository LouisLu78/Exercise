# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/11/24
'''
Exercise 7.1. Make a function class. Make a class F that implements the function
f(x; a, w) = e−ax sin(wx). A value(x) method computes values of f, while a and w are class
attributes. Test the class with the following main program:
from math import *
f = F(a=1.0, w=0.1)
print f.value(x=pi)
f.a = 2
print f.value(pi)

class F:
    def __init__(self, a, w):
        self.a= a
        self.w= w

    def value(self, x):
        from math import exp, sin, pi
        a, w=self.a, self.w
        return exp(-a*x)*sin(w*x)


from math import *

f = F(1, 0.1)
print(f.value(pi))
f.a = 2
print (f.value(pi))'''

'''
Exercise 7.3. Make classes for a rectangle and a triangle.
a rectangle with width W, height H, and lower left corner (x0, y0); and a general
triangle specified by its three vertices (x0, y0), (x1, y1), and (x2, y2) as
explained in Exercise 3.9. Provide three methods: __init__ (to initialize
the geometric data), area, and circumference

class Triangle:
    def __init__(self, W, H):
        self.W,self.H=W, H
       
    def area(self):
        W,H=self.W,self.H
        return 0.5*W*H

    def circumference(self):
        from math import sqrt
        x0, y0, x1, y1, x2, y2=self.x0,self.y0,self.x1, self.y1, self.x2, self.y2
        L1=sqrt((x1-x0)**2+(y1-y0)**2)
        L2=sqrt((x2-x1)**2+(y2-y1)**2)
        L3=sqrt((x2-x0)**2+(y2-y0)**2)
        return L1+L2+L3
        
t=Triangle(W=4, H=3)
t.x0,t.y0,t.x1,t.y1,t.x2,t.y2=0,0,4,0,0,3
print('The area of the triangle is %.2f.'%t.area())
print('The circumference of the triangle is %.2f.'%t.circumference())'''

'''Exercise 7.6. Make a class for quadratic functions.
Consider a quadratic function f(x; a, b, c) = ax2 + bx + c. Make a class Quadratic for representing f, where a, b, and c are attributes, and
the methods are
1. value for computing a value of f at a point x,
2. table for writing out a table of x and f values for n x values in the interval [L, R],
3. roots for computing the two roots.

class Quadratic:
    def __init__(self,a,b,c):
        self.a, self.b, self.c = a, b, c

    def value(self,x):
        a, b, c=self.a, self.b, self.c
        return a*x**2+b*x+c

    def table(self,n):
        L,R=self.L,self.R
        step=(R-L)/(n-1)
        for i in range(n):
            x=L+i*step
            print('%10.3f,%10.3f'%(x, self.value(x)))

    def root(self):
        from math import sqrt
        a, b, c = self.a, self.b, self.c
        delta=b**2-4*a*c
        if delta>=0:
            x1,x2=(-b+sqrt(delta))/(2*a),(-b-sqrt(delta))/(2*a)
        else:
            delta*=-1
            x1=complex(-b/(2*a),sqrt(delta)/(2*a))
            x2=complex(-b/(2*a),-sqrt(delta)/(2*a))

        return x1, x2

q=Quadratic(1,-2,-1)
print('f(-1) =',q.value(-1))
q.L,q.R=-2,2
q.table(10)
print(q.root())
q2=Quadratic(1,-2,5)
print(q2.root())'''

'''
Exercise 7.10. Deduce a class implementation. Write a class Hello that behaves as illustrated in the following session:
>>> a = Hello()
>>> print a(’students’)
Hello, students!
>>> print a
Hello, World!

class Hello:

    def __call__(self, message):
            return 'Hello,{}!'.format(message)

    def __str__(self):
            return 'Hello, World!'

a = Hello()
print (a('students'))
print (a)
print (a('snow'))'''

'''
Exercise 7.11. Use special methods in Exer. 7.1.Modify the class from Exercise 7.1 such that the following code works:
f = F2(1.0, 0.1)
print f(pi)
f.a = 2
print f(pi)
print f

class F2:
    def __init__(self, a, w):
        self.a= a
        self.w= w

    def __call__(self, x):
        from math import exp, sin, pi
        a, w=self.a, self.w
        return exp(-a*x)*sin(w*x)

    def __str__(self):
        return str(f(pi))

from math import *

f = F2(1, 0.1)
print(f(pi))
f.a = 2
print (f)'''

'''
Exercise 7.13. Implement a class for numerical differentiation.
A widely used formula for numerical differentiation of a function f(x) takes the form(7.7)
The goal of this exercise is to use the formula (7.7) to automatically differentiate a mathematical function f(x) implemented as a Python
function f(x).Implement class Central and include an optional argument h to the constructor in class Central so
that one can specify the value of h in the approximation (7.7)

class Central:
    def __init__(self,f,h=1E-5):
        self.f,self.h=f,h

    def __call__(self,x):
        h=self.h
        return (f(x + h) - f(x-h)) /(2*h)

def f(x):
    return 0.25*x**4
df = Central(f)
for x in (1, 5, 10):
    df_value = df(x)
    exact = x**3
    print("f’(%d)=%g (error=%.2E)" % (x, df_value, exact-df_value))

def f(x):
    from math import log as ln
    return ln(x)
df=Central(f)
x=10
for df.h in (0.5, 0.1, 1E-3, 1E-5, 1E-7, 1E-9, 1E-11):
    df_value = df(x)
    exact = 1/x
    print("h=%g, f’(%d)=%g (error=%.2E)" % (df.h, x, df_value, exact - df_value))'''

'''
Exercise 7.17. Make a class for summation of series.
Our task in this exercise is to calculate a sum S(x) = N k=M fk(x),
where fk(x) is a term in a sequence which is assumed to decrease in absolute value. In class Sum, for computing S(x), the constructor requires the following three arguments: 
fk(x) as a function f(k, x), M as an int object M, and N as an int object N. A __call__ method computes and returns S(x). The next term in the series, fN+1(x), should
be computed and stored as an attribute first_neglected_term......Calculate by hand what the output of this test becomes, and use it to
verify your implementation of class Sum.

class Sum:
    def __init__(self,term,M,N,first_neglected_term=None):
        self.term,self.M,self.N=term,M,N

    def __call__(self, x):
        term, M, N=self.term,self.M,self.N
        # self.first_neglected_term = term(N + 1, x)
        return sum(term(k,x) for k in range(M,N+1) )
    def first(self):
        term, N = self.term, self.N
        self.first_neglected_term = term(N + 1, x)
        return self.first_neglected_term

def term(k, x):
    return (-x)**k

S = Sum(term, M=0, N=100)
x = 0.5
print (S(x))
S.first()
print (S.first_neglected_term)'''

'''
Exercise 7.27. Vectorize a class for numerical integration.Implement a vectorized version of the Trapezoidal rule in class
Integral from Chapter 7.3.3. Use sum to compute the sum in the formula, and allow for either Python’s built-in sum function or for the
sum function from numpy.


class Integral:
    def __init__(self, f, a, n=100):
        self.f, self.a, self.n = f, a, n

    def trapezoidal(self, f, a, x, n):

        h = (x - a) / n
        I = 0.5 * (f(a)+f(x))
        I+= sum(f(a + i * h)for i in range(1, n))
        I *= h
        return I

    def __call__(self, x):
        return self.trapezoidal(self.f, self.a, x, self.n)

def f(x):
    from math import sin
    return sin(x)
G=Integral(f,0)
result=G(10)
print(result)'''


# import sys
# sys.path.append(r'D:\Program files\JetBrains\my_module')
# from deriv_central import Central
# from math import sin, pi
#
# def f1(x):
#     return sin(x)
# df=Central(f1)
# print(df(pi/4))

'''
Exercise 7.42. Find local and global extrema of a function.
Extreme points of a function f(x) are normally found by solving
f (x) = 0. A much simpler method is to evaluate f(x) for a set of
discrete points in the interval [a, b] and look for local minima and
maxima among these points. We work with n equally spaced points
a = x0 < x1 < · · · < xn−1 = b, xi = a + ih, h = (b − a)/(n − 1).
1. First we find all local extreme points in the interior of the domain.
Local minima are recognized by
f(xi−1) > f(xi) < f(xi+1), i = 1, . . . , n − 2.
Similarly, at a local maximum point xi we have
f(xi−1) < f(xi) > f(xi+1), i = 1, . . . , n − 2.
We let Pmin be the set of x values for local minima and Fmin the
set of the corresponding f(x) values at these minimum points. Two
sets Pmax and Fmax are defined correspondingly, containing the maximum points and their values.
2. The boundary points x = a and x = b are for algorithmic simplicity
also defined as local extreme points: x = a is a local minimum if
f(a) < f(x1), and a local maximum otherwise. Similarly, x = b is a
local minimum if f(b) < f(xn−2), and a local maximum otherwise.
The end points a and b and the corresponding function values must
be added to the sets Pmin, Pmax, Fmin, Fmax.
3. The global maximum point is defined as the x value corresponding
to the maximum value in Fmax. The global minimum point is the x
value corresponding to the minimum value in Fmin.
Make a class MinMax with the following functionality:

class MinMax:
    def __init__(self,f,a,b,n):
        self.f,self.a,self.b,self.n=f,a,b,n
        self._find_extrema()

    def _find_extrema(self):
        f,a,b,n=self.f,self.a,self.b,self.n
        h = (b-a)/(n-1)
        Pmin=set()
        Fmin=set()
        Pmax =set()
        Fmax =set()

        for i in range(1,n-1):
            x=a+i*h
            if f(x)<f(x-h)and f(x)<f(x+h):
                Pmin.add(round(x,4)), Fmin.add(round(f(x),4))
            elif f(x)>f(x-h)and f(x)>f(x+h):
                Pmax.add(round(x,4)), Fmax.add(round(f(x),4))
        if f(a)<f(a+h):
            Pmin.add(a), Fmin.add(round(f(a),4))
        elif f(a)>f(a + h):
            Pmax.add(a),Fmax.add(round(f(a),4))
        if f(b)<f(b-h):
            Pmin.add(b), Fmin.add(round(f(b),4))
        elif f(b)>f(b-h):
            Pmax.add(b), Fmax.add(round(f(b),4))
        if len(Pmin)==0:
            print('It\'s a horizontal line.')
        elif len(Pmin)==1 and len(Pmax)==1:
            print('It\'s monotonous.')
        else:
            global_min=min(Fmin)
            global_max = max(Fmax)
            self.Pmin, self.Fmin, self.global_min=Pmin, Fmin, global_min
            self.Pmax, self.Fmax, self.global_max=Pmax, Fmax, global_max
            return [Pmin, Fmin, Pmax, Fmax]

    def get_global_minimum(self):
        f=self.f
        return [x for x in self.Pmin if f(x)==self.global_min]

    def get_global_maximum(self):
        f = self.f
        return [x for x in self.Pmax if f(x)==self.global_max]

    def get_all_minima(self):
        f=self.f
        return [(x,f(x)) for x in self.Pmin]

    def get_all_maxima(self):
        f = self.f
        return [(x,f(x)) for x in self.Pmax]

    def __str__(self):
        return 'All minima:%s\nAll maxima:%s\nGlobal minimum:%f\nGlobal maximum:%f'\
               %(str(self.Pmin), str(self.Pmax), self.global_min, self.global_max)


def _verify():
    from math import exp, sin, pi
    def f1(x):
        return x ** 2 * exp(-0.2 * x) * sin(2 * pi * x)
    m = MinMax(f1, 0, 4, 5001)
    print(m)

    def f2(x):
        return x**2
    m = MinMax(f2, 0, 4, 1001)

    def f3(x, t=0):
        p = exp(-(x - 3 * t) ** 2)
        c = sin(3 * pi * (x - t))
        return p * c
    m = MinMax(f3, -4, 4, 5000)
    print(m)

if __name__=='__main__':
    _verify()'''

'''Exercise 7.44. Find the optimal production for a company.

class Prod:
    def __init__(self,x,y):
        self.x,self.y=int(x),int(y)

    def f(self):
        x, y=self.x, self.y
        return 45*x+14*y

    def condition(self):
        x, y = self.x, self.y
        if x>=0 and y>=0 and (2*x+y<=100) and (5*x+3*y<=80) and (4*y<=150):
            return True
        else:
            return False

import numpy as np
import matplotlib.pyplot as plt

T=set()
alpha=set()
for x in range(100):
    for y in range(100):
        p=Prod(x,y)
        if p.condition():
            T.add((x,y))
            alpha.add(p.f())
print('The maximum revenue of Prod company is %d.'%max(alpha))
a_array=np.array(list(T)).reshape(-1,2)
print(a_array)
x,y=a_array[:,0],a_array[:,1]

plt.title('The possible product of company Prod')
plt.scatter(x,y)
plt.show()'''

'''
Exercise 9.1. Demonstrate the magic of inheritance.
Consider class Line from Chapter 9.1.1 and a subclass Parabola0 defined as
class Parabola0(Line):
pass
That is, class Parabola0 does not have any own code, but it inherits from class Line. Demonstrate in a program or 
interactive session, using methods from Chapter 7.5.5, that an instance of class Parabola0 contains everything 
(i.e., all attributes and methods) that an instance of class Line contains.

class Line:
    def __init__(self,c0,c1):
        self.c0,self.c1 = c0,c1

    def __call__(self, x):
        c0, c1 = self.c0,self.c1
        return c0+c1*x

    def dump(self):
        print(self.__dict__)

    def table(self, L, R, n):
        s=''
        import numpy as np
        for x in np.linspace(L, R, n):
            y = self(x)
            s +='%12g %12g\n' %(x, y)
        return s

class Parabola0(Line):
    pass
p0=Parabola0(-5,2)
print(p0.dump())

'''
# Exercise 9.2. Inherit from classes in Ch. 9.1.
# The task in this exercise is to make a class Cubic for cubic functions
# c3x3 + c2x2 + c1x + c0
# with a call operator and a table method as in classes Line and Parabola from Chapter 9.1. Implement class Cubic by inheriting from class
# Parabola, and call up functionality in class Parabola in the same way as class Parabola calls up functionality in class Line.
# Make a similar class Poly4 for 4-th degree polynomials
# c4x4 + c3x3 + c2x2 + c1x + c0
# by inheriting from class Cubic. Insert print statements in all the __call__ to help following the program flow. Evaluate cubic and a
# 4-th degree polynomial at a point, and observe the printouts from all the superclasses.
'''
class Parabola(Line):
    def __init__(self, c0, c1, c2):
        Line.__init__(self,c0,c1)
        self.c2=c2

    def __call__(self, x):
        c2=self.c2
        return Line.__call__(self,x)+c2*x**2
        
p=Parabola(5,-1,2)
print(p(2))
print(p.table(-5,5,10))

class Cubic(Parabola):
    def __init__(self, c0, c1, c2, c3):
        Parabola.__init__(self,c0,c1,c2)
        self.c3 = c3

    def __call__(self, x):
        c3=self.c3
        return Parabola.__call__(self,x)+c3*x**3

c=Cubic(-10,8,-1,5)
print(c(-1))
print(c.table(-5,5,10))

class Poly4(Cubic):
    def __init__(self, c0, c1, c2, c3, c4):
        Cubic.__init__(self,c0,c1,c2,c3)
        self.c4 = c4

    def __call__(self, x):
        c4=self.c4
        return Cubic.__call__(self,x) +c4*x**4
        
f=Poly4(-10,8,-1,5,2)
print(f(1))
print(f.table(-5,5,10))

'''
# Exercise 9.3. Inherit more from classes in Ch. 9.1.
# Implement a class for the function f(x) = A sin(wx) + ax2 + bx + c.
# The class should have a call operator for evaluating the function for some argument x, and a constructor that takes the
# function parameters A, w, a, b, and c as arguments. Also a table method as in classes Line and Parabola should be present.
# Implement the class by deriving it from class Parabola and call up functionality already implemented in class Parabola whenever possible.
'''
class Mix(Parabola):
    def __init__(self,A,w,a,b,c):
        Parabola.__init__(self,c,b,a)
        self.A, self.w = A, w

    def __call__(self,x):
        from math import sin
        A, w = self.A, self.w
        p=Parabola.__call__(self,x)
        self.p=p
        return p+A*sin(w*x)

m=Mix(2,1,2,-1,5)
print(m(3))
print(m.p)
print(m.table(-5,5,10))'''

'''
Exercise 9.7. Modify a function class by subclassing.
Consider the VelocityProfile class from page 350 for computing the function v(r; β, μ0, n, R) in formula (5.23) on page 252. 
Suppose we want to have v explicitly as a function of r and n (this is necessary if we want to illustrate how the velocity 
profile, the v(r) curve, varies as n varies). We would then like to have a class VelocityProfile2 that is initialized
with β, μ0, and R, and that takes r and n as arguments in the __call__ method. Implement such a class by inheriting from class
VelocityProfile and by calling the __init__ and value methods in the superclass. It should be possible to try the class out
with the following statements:
v = VelocityProfile2(beta=0.06, mu0=0.02, R=2)
# Evaluate v for various n values at r=0
for n in 0.1, 0.2, 1:
print v(0, n)

class VelocityProfile: #The codes excerpted from the textbook
    def __init__(self, beta, mu0, n, R):
        self.beta, self.mu0, self.n, self.R = beta, mu0, n, R

    def value(self, r):
        beta, mu0, n, R = self.beta, self.mu0, self.n, self.R
        v = (beta/(2.0*mu0))**(1/n)*(n/(n+1))*\
        (R**(1+1/n) - r**(1+1/n))
        return v

for n in [0.1, 0.2, 1]:
    v=VelocityProfile(0.06, 0.02, n, 2)
    print(n, v.value(0))

class VelocityProfile2(VelocityProfile):#the codes made by myself according to the requirement of the question 
    def __init__(self, beta, mu0, R):
        VelocityProfile.__init__(self, beta, mu0, None, R)

    def __call__(self, r, n):
        self.n=n
        return VelocityProfile.value(self,r)

v = VelocityProfile2(beta=0.06, mu0=0.02, R=2)
for n in [0.1, 0.2, 1]:
    print('%12g %12g'%(n, v(0, n)))'''

'''
Exercise 9.15. Change the user interface of a class hierarchy.
All the classes in the Integrator hierarchy from Chapter 9.3 take the integration limits a and b plus the number
of integration points n as input to the constructor. The integrate method takes the function to integrate, f(x), as 
parameter. Another possibility is to feed f(x) to the constructor and let integrate take a, b, and n as parameters. 
Make this change to the integrate.py file with the Integrator hierarchy.

class Integrator: # the answer shown in the textbook
    def __init__(self, a, b, n):
        self.a, self.b, self.n = a, b, n
        self.points, self.weights = self.construct_method()

    def construct_method(self):
        raise NotImplementedError('no rule in class %s' %
        self.__class__.__name__)

    def integrate(self, f):
        s = 0
        for i in range(len(self.weights)):
            s += self.weights[i]*f(self.points[i])
        return s

class Midpoint(Integrator):
    def construct_method(self):
        a, b, n = self.a, self.b, self.n # quick forms
        h = (b-a)/n
        x = np.linspace(a + 0.5*h, b - 0.5*h, n)
        w = np.zeros(len(x)) + h
        return x, w
#below is my answer to the question

class New_integrator:
    def __init__(self, f):
        self.f=f
        self.points, self.weights = self.construct_method()

    def construct_method(self):
        raise NotImplementedError('no rule in class %s' %
                                      self.__class__.__name__)

    def integrate(self, a, b, n):
        start, end, num=a, b, n
        for i in range(n):
            s+=self.weights[i]*value[i]
        return s

class Trapezoidal(New_integrator):
    def construct_method(self):
        f=self.f   
        step=(end-start)/(num-1)     
        v = np.linspace(f(start), f(end), num)
        w = np.zeros(n) + step
        return w, v'''





