import urllib.request

response = urllib.request.urlopen("http://www.fishc.com")#打开网页
html = response.read()#读取网页
html = html.decode("utf - 8")#解码网页
print(html,response.getcode(),response.geturl(),response.info())

req = urllib.request.Request("http://ws4.sinaimg.cn/mw600/006wH16pgy1g2ie224oy0j31201eo7wh.jpg")
response = urllib.request.urlopen(req)
cat_img = response.read()
with open('cat_200_300.jpg','wb') as f:
    f.write(cat_img)

