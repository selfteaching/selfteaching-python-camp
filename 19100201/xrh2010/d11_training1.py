import requests
import getpass
import yagmail
from pyquery import PyQuery
from mymodule import stats_word

# 提取微信公众号正文
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(response.text) 
content = document('#js_content').text()

# 应用 stats_word 方法提取前100个词
day11 = stats_word.stats_text_cn(content)
content = day11.most_common(100)
day11_1 = str(day11)
# print(day11_1)

# 设置邮箱
user = input('请输入你的邮箱:') #邮箱账号
password = getpass.getpass('请输入发件人邮箱密码(可复制粘贴)：') #邮箱开通smtp服务授权码
recipient = input('请输入收件人邮箱:')
smtp = "smtp.163.com" #服务器地址
# print(user,password,recipient)  #检查

# 发送邮件
yag = yagmail.SMTP(user,password,smtp)
yag.send(recipient,'19100101 sundyyang',day11_1)