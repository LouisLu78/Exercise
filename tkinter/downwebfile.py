import requests
res=requests.get('http://c.biancheng.net/view/2457.html', stream=True)
rescode=res.raise_for_status()
# print(rescode)
with open('Tkinter06.html', 'wb') as tb:
    for chunk in res.iter_content(100000):
        tb.write(chunk)
    # tb.write(res.content)



