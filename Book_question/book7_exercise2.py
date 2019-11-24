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
        # self.x1,self.y1,self.x2,self.y2=x1, y1, x2, y2

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
3. roots for computing the two roots.'''

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
            x2 = complex(-b/(2*a), -sqrt(delta)/(2*a))

        return x1, x2

q=Quadratic(1,-2,-1)
print('f(-1) =',q.value(-1))
q.L,q.R=-2,2
q.table(10)
print(q.root())
q2=Quadratic(1,-2,5)
print(q2.root())



