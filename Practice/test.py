# -*- coding:utf-8 -*-
# author: Guangqiang Lu time:2019/11/29
# If not explicitly pointed out, all the codes are written by myself.

import sys
sys.path.append(r'D:\Program files\JetBrains\my_module')
import bs4, requests
import re, os, shutil
from pdf_convertor_v2 import *

print(sys.path)

# from pdf_convertor import *
# url = 'https://blog.csdn.net/slhlde/article/details/81937838'
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:70.0) Gecko/20100101 Firefox/70.0'}
# response = requests.get(url,headers=headers)
# response.raise_for_status()
# with open('bs4.html', 'wb') as f:
#     for chunk in response.iter_content(100000):
#         f.write(chunk)
# html_to_pdf('bs4.html',"C:\\Users\\Basanwei\\Downloads\\pdf\\bs4text.pdf")
# soup=bs4.BeautifulSoup(response.content, 'html.parser')
# print(soup)
#
# tags = soup.select('a')
# print(tags)

# for tag in tags:
# 	print(tag['href'])

# from pdf_convertor import *
# urls =['https://mp.weixin.qq.com/s/OHl_mFfOOv6Ny7lUzK-GLw', 'https://mp.weixin.qq.com/s/1oFf0vXf-vVcSAeBzE-FeA',
#         'https://mp.weixin.qq.com/s/nEJG5lTawEmyrv5CBKjiOQ', 'https://mp.weixin.qq.com/s/xOmF3JSfGrthhd-qsLQ3oQ',
#         'https://mp.weixin.qq.com/s/dPqycJjFoajTxLMHoQpC5A']
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:70.0) Gecko/20100101 Firefox/70.0'}
# count=1
# for url in urls:
#     url_to_pdf(url,"C:\\Users\\Basanwei\\Downloads\\pdf\\temp{}.pdf".format(count))
#     count+=1
#     print('File no.%d is done.'%count)

html_file='D:\\Arbeiten\\myfiles\\favorites_2019_11_27.html'
pdffolder = "C:\\Users\\Basanwei\\Downloads\\pdf"
f=open(html_file,'r+', encoding='UTF-8')
regex0=re.compile(r'Python100')
regex1=re.compile(r'weixin')
urls=[]

soup=bs4.BeautifulSoup(f.read(),'html.parser')
'''
# old version is: tags=soup.select('a')
for tag in tags:
	if regex.search(tag['href']) is not None:
		urls.append(tag['href'])
'''
tags=soup.find_all(['h3','a'])
t=list(tags)
f.close()
for i,v in enumerate(t):
    if regex0.search(str(v)):
        position=i
        print(position)
        break
for i in range(position+1,len(t)):
    if regex1.search(str(t[i])):
        urls.append(t[i]['href'])
count=0
print(len(urls))
for url in urls:
	pdffile= os.path.join(pdffolder, '0%d_.pdf'%count)
	target=Convertor().url_to_pdf(url)
	shutil.copy(target, pdffile)
	count+=1
	print('The No.%d file is downloaded.'%count)
	os.unlink(target)