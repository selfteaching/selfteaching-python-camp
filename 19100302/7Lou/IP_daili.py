import urllib.request
import re
import requests
try:
    requests.get('https://wwww.whatismyip.com', proxies={'http':'117.68.192.78:18118'})
except:
    print ('connect failed')
else:
    print( 'success')
url = 'https://wwww.whatismyip.com'
proxy_support = urllib.request.ProxyHandler({'http':'117.68.192.78:18118'})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'),('cookie','__cfduid=d016cd7add055804c16db65cf36ff5a261556209534; dwqa_anonymous=1k6mzDX5HKwbwJwUXDPQPFDA3AYPmzR4HBdP0PWbDiC; _ga=GA1.2.537112796.1556209536; _gid=GA1.2.1370345645.1556209536; __gads=ID=d146e2f1d8084290:T=1556209798:S=ALNI_Mb3v0CBflI2gyfFqTTxYSI_XCtlfg')]
urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('gbk')
print(html)

