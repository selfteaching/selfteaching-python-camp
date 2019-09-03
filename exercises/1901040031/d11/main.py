
from mymodule import stats_word as s                                #从模块中导入自定义函数
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #禁用安全证书，解决InsecureRequestWarning

url='https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'
response = requests.get(url)                                        # 最基本的GET请求


from pyquery import PyQuery
document = PyQuery(response.text)
content =document('#js_content').text()                              #从网页中导出文本

results= s.stats_text_cn(content,100)                                #调用函数，统计词频
r_string= ''.join(str(i)for i in results)                            #列表转化为字符串
print(r_string)

import yagmail                                                       #通过邮箱发送内容                      
import getpass

sender= input('输入发件人邮箱:')
password = getpass.getpass('请输入发件人邮箱密码(可复制粘贴)：')        #在填写授权码时，是不会出现东西的，只要一口气把它输完就好
recipients= input('输入收件人邮箱：')
yag= yagmail.SMTP(sender, password,'smtp.163.com' ).send(recipients,'自学训练营3群+zhangmmmin', r_string)


try:                                 #try except  捕获异常
    print(s.stats_text_cn(content,100))
except ValueError as err:
    print("err:not string ,try again")

