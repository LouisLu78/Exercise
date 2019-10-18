# -*- coding:utf-8 -*-
import re
message='My mobile number is 86-13966666666.'
# mobile_regre=re.compile(r'\d\d-\d\d\d\d\d\d\d\d\d\d\d')
# mobile_regre=re.compile(r'(\d){2}-(\d){11}')
mobile_regre=re.compile(r'(\d){1,3}-(\d){9,12}')
mobile_regre1=re.compile(r'(\d){1,3}-(\d){9,12}?')
mo=mobile_regre.search(message)
mo1=mobile_regre1.search(message)
print(mo.group())
print(mo1.group())