# -*- coding:utf-8 -*-
# author: Guangqiang Lu time:2019/11/29
# If not explicitly pointed out, all the codes are written by myself.

import bs4, requests
import re, os, shutil
from pdf_convertor_v2 import *


html_file='D:\\Arbeiten\\myfiles\\favorites_2019_11_27.html'
pdffolder = "C:\\Users\\Basanwei\\Downloads\\pdf"
f=open(html_file,'rb')
regex=re.compile(r'https://mp\.(.*)')
urls=[]
count=71
soup=bs4.BeautifulSoup(f.read(), 'html.parser')
tags=soup.select('a')
for tag in tags:
	if regex.search(tag['href']) is not None:
		urls.append(tag['href'])
for url in urls[-1:-12:-1]:
	pdffile= os.path.join(pdffolder, '0%d_.pdf'%count)
	Convertor().url_to_pdf(url)
	shutil.move(os.path.join(pdffolder, 'tmp%d.pdf'%Convertor.counter), pdffile)
	count-=1
	print('The No.%d file is done'%count)
f.close()


# url = 'https://mp.weixin.qq.com/s?__biz=MzU1NDk2MzQyNg==&mid=2247484049&idx=2&sn=26f28abcdefd030f2fc294f9cca9d140&chksm=fbdada1cccad530a4b619aa4cc2ea75886d02aa0b2d244029e2ac2cffd67e284ea13494c0ed8&scene=21#wechat_redirect'
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:70.0) Gecko/20100101 Firefox/70.0'}
# response = requests.get(url,headers=headers)
# soup=bs4.BeautifulSoup(response.content, 'html.parser')
#
# tags = soup.select("a", text="python")
#
# for tag in tags:
# 	print(tag['href'])





