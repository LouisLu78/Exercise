# -*- coding:utf-8 -*-
import numpy as np
a=range(1,11)
b=range(10,0,-1)

c1=range(1,13)
c2=range(11,-1,-1)
c3=range(12,0,-1)
# ab=list(a)+list(b)

vector=np.array(list(a))
print(vector)
print(np.size(vector))
print(vector.dtype)

matrix=np.array([list(a),list(b)])
print(matrix)
print(np.size(matrix))
print(matrix.dtype)

h=np.array([list(c1),list(c2),list(c3)])
print(h,h.shape)
print(np.size(h))
print(h.dtype)

hseg1=h[1:3,2:4]
print(hseg1,hseg1.shape)


hseg2=h[[1,1,0],[2,4,5]]
print(hseg2,hseg2.shape)

print(h[h>6])
print(h[1],h[:,0])
# condition=h>3 and h<9
# print(condition)
hseg3=h[0:2,6:8]
print(hseg3,hseg3.shape)

x=np.array(hseg1,dtype=np.float64)
y=np.array(hseg3,dtype=np.float64)
# x=np.array(hseg1,dtype=float)
# y=np.array(hseg3,dtype=float)

print(np.add(x,y))
print(np.subtract(x,y))
print(np.multiply(x,y))
print(np.divide(x,y))
print(np.sqrt(x))
print(np.sqrt(y))


#today's new course about the dot multiplication of two matrix.20191016
print(x.dot(y))
print(np.dot(x,y)) #np.dot
print(np.sum(x),np.sum(y))
print(np.sum(y,axis=0),np.sum(y,axis=1))
# print(h.T)
# print(x+[1,3]) #broadcasting
z=np.empty_like(y)
print(z)