# -*- coding:utf-8 -*-
# author: Guangqiang Lu time:2019/11/29
# If not explicitly pointed out, all the codes are written by myself.

import bs4, requests
import re, os, shutil
from pdf_convertor_v2 import *



# html_file='D:\\Arbeiten\\myfiles\\favorites_2019_11_27.html'
# pdffolder = "C:\\Users\\Basanwei\\Downloads\\pdf"
# f=open(html_file,'rb')
# regex=re.compile(r'https://mp\.(.*)')
# urls=[]
# count=71
# soup=bs4.BeautifulSoup(f.read(), 'html.parser')
# tags=soup.select('a')
# for tag in tags:
# 	if regex.search(tag['href']) is not None:
# 		urls.append(tag['href'])
# for url in urls[-1:-12:-1]:
# 	pdffile= os.path.join(pdffolder, '0%d_.pdf'%count)
# 	target=Convertor().url_to_pdf(url)
# 	shutil.copy(target, pdffile)
# 	count-=1
# 	print('The No.%d file is downloaded.'%count)
# 	os.unlink(target)
# f.close()


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

