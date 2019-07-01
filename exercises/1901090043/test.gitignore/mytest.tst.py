import requests
from pyquery import PyQuery
 
url = 'https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'
response = requests.get(url,verify = False)

document = PyQuery(response.text) 
content = document('#js_content').text()
print(content)