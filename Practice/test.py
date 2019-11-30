# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/11/29
# If not explicitly pointed out, all the codes are written by myself.

import bs4, requests
import re, os
from pdf_convertor import *


html_file='D:\\Arbeiten\\myfiles\\favorites_2019_11_27.html'
pdffolder = "C:\\Users\\Basanwei\\Downloads\\pdf"
f=open(html_file,'rb')
regex=re.compile(r'https://mp\.(.*)')
urls=[]
count=71
soup=bs4.BeautifulSoup(f.read(), 'html.parser')
tags = soup.select("a")
for tag in tags:
	if regex.search(tag['href']) is not None:
		urls.append(tag['href'])
for url in urls[-1:-72:-1]:
	pdffile= os.path.join(pdffolder, '第%d天.pdf'%count)
	url_to_pdf(url,pdffile)
	count-=1
	print('The No.%d file is done'%count)
f.close()
