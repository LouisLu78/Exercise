import bs4, webbrowser, sys, requests

print('searching in baidu...')
res=requests.get('http://www.baidu.com/s?wd=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
# print(res.text[:1000])
soup=bs4.BeautifulSoup(res.text)
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://www.baidu.com' + linkElems[i].get('href'))