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
print(h)
print(np.size(h))
print(h.dtype)

hseg1=h[1:3,2:4]
print('the small matrix is: ',hseg1)

hseg2=h[[1,1,0],[2,4,5]]
print(hseg2)

print(h[h>6])
print(h[1],h[:,0])
# condition=h>3 and h<9
# print(condition)