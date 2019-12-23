# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/4
# If not explicitly pointed out, all the codes are written by myself.
import sys
sys.path.append(r'D:\Program files\JetBrains\my_module')
from vectors_angle import *

x1=(-1,0,1)
y1=(1,0,1)
angle1=angle(x1,y1)
x2=(0,1,1)
y2=(1,1,0)
angle2=angle(x2,y2)
x3=(3,0,1)
y3=(0,0,2)
angle3=angle(x3,y3)
print('angle1=%.2f, angle2=%.2f, angle3=%.2f'%(angle1, angle2, angle3))
x4=(2,2,1)
y4=(0,1,0)
print('The angle you are calculating is %.2f degree.'%angle(x4,y4))
print(angle((1,0,0),(2,2,1)))