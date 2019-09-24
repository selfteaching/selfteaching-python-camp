# 先导入第三方库
import yagmail, requests, pyquery, getpass
from pyquery import PyQuery
from  mymodule import stats_word

#实现邮箱和密码的输⼊
sender = input('输⼊入发件⼈人邮箱:')
password = getpass.getpass('输⼊入发件⼈人邮箱密码(可复制粘贴):') #填授权码
recipients = input('输⼊入收件⼈人邮箱:') #pythoncamp@163.com

#提取正文
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA') #获取该网页内容
document = PyQuery(response.text) 
content = document('#js_content').text() #将网页内容转换成文本

#分词统计
word_list = stats_word.stats_text_cn(content, 100)
word_str = str(word_list) #stat: path should be string, bytes, os.PathLike or integer, not tuple

#发送邮件
yag = yagmail.SMTP(sender, password, 'smtp.qq.com') #发件人，密码以及服务器
yag.send(recipients, '【1901100206】自学训练营18群 DAY11 dexiangjoy', word_str)