import requests
res=requests.get('http://c.biancheng.net/view/2457.html')
res.raise_for_status()
Tkinterfile=open('Tkinter06.html', 'wb')
for chunk in res.iter_content(100000):
    Tkinterfile.write(chunk)
Tkinterfile.close()


