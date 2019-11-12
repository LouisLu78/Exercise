# -*- coding:utf8 -*-
# import bs4, webbrowser, sys, requests

# print('searching in baidu...')
# res=requests.get('http://www.baidu.com/s?wd=' + ' '.join(sys.argv[1:]))
# res.raise_for_status()
# # print(res.text[:1000])
# soup=bs4.BeautifulSoup(res.text)
# print(soup)
# linkElems = soup.select('.b a')
# numOpen = min(5, len(linkElems))
# for i in range(numOpen):
#     webbrowser.open('http://www.baidu.com' + linkElems[i].get('href'))



# import docx
# mydoc123=docx.Document("D:\\Arbeiten\\myfiles\\Arbeiten\\学术评论之一百二十三.docx")
# print('Mydoc123 contains {} paragraghs'.format(len(mydoc123.paragraphs)))
# for i in range(len(mydoc123.paragraphs)):
#     print('This is the paragraph {}...'.format(i+1))
#     print(mydoc123.paragraphs[i].text, end='\n')
# print(mydoc123.paragraphs[1].text)
# print('Paragragh 1 contains {} runs'.format(len(mydoc123.paragraphs[1].runs)))
# print(mydoc123.paragraphs[1].runs[1].text)
#
# def retrive_text(file):
#     doctext=docx.Document(file)
#     fulltext=[]
#     for para in doctext.paragraphs:
#         fulltext.append(para.text)
#     return '\n'.join(fulltext)
# doc123= retrive_text("D:\\Arbeiten\\myfiles\\Arbeiten\\学术评论之一百二十三.docx")
# print(doc123)
# print(len(str(doc123)))
# import docx
# with open('downfile.txt','r') as f:
#     cont=f.read()
# newdoc=docx.Document()
# newdoc.add_paragraph(cont)
# newdoc.save('downfile.docx')

# def cal(n):
#     result=1
#     for i in range(1,n):
#         result*=i
#     return result
# import time
# start=time.time()
# product=cal(100000)
# end=time.time()
# print('The result has {} digits.'.format(len(str(product))))
# print('It takes {} seconds to finish the process.'.format(end-start))

# import datetime
# dt=datetime.datetime.today()
# now=datetime.datetime.now()
# print(dt)
# print(now)
#
# import subprocess
# subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\hello.txt'])


import requests, webbrowser
import shutil, os, random
import datetime

today=datetime.datetime.now()
Today=today.strftime('%Y_%m_%d')
newsfolder="C:\\Users\\Basanwei\\Downloads\\news"
if not os.path.exists(newsfolder):
    os.makedirs(newsfolder)

urls={'Yahoo':'http://news.yahoo.com','MSN':'http://www.msn.com/en-us/news/world',
    'FOX':'https://www.foxnews.com/world', 'CNN':'https://edition.cnn.com/world'}

for url in urls.items():
    res=requests.get(url[1], stream=True)
    if res.status_code ==200:
        print('The website for {} is connected.'.format(url[0]))
        with open('news.html', 'wb') as tb:
            for chunk in res.iter_content(100000):
                tb.write(chunk)
        filename=os.path.join(newsfolder, '{}_news_{}.html'.format(url[0], Today))
        shutil.move('news.html', filename)
        print('done')
    else:
        print('The internet connection for {} doesn\'t work today.'.format(url[0]))

print('Enjoy yourself in reading today\'s news.')

newsurl=random.sample(list(urls.values()),2)
for url in newsurl:
    webbrowser.open(url)

