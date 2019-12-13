# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/6
# If not explicitly pointed out, all the codes are written by myself.

m=map(lambda x:x**2, range(10))
f=filter(lambda x:x%2==1,range(10))
print(list(m))
print(list(f))

import sys
print(sys.path)