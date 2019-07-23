from mymodule import stats_word
import requests
from pyquery import PyQuery
import getpass
import yagmail

r = requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")

document = PyQuery(r.text)
content = document('#js_content').text()

word_list = stats_word.stats_text_cn(content, 20)
mail_content = ""
for x in word_list:
    mail_content += "{}: {}\n".format(x[0], x[1])
print(mail_content)

sender = input('输⼊发件⼈邮箱:')
password = getpass.getpass('输⼊发件⼈邮箱密码(可复制粘贴):')
recipients = 'pythoncamp@163.com'
# recipients = input('输⼊收件⼈邮箱:')

"""
sender = 'q86155779@163.com'
password = '**********'
recipients = '532820370@qq.com'
"""

yag = yagmail.SMTP(user=sender, password=password, host='smtp.163.com')
# contents = [mail_content]
r = yag.send(recipients, '自学训练营学习9群 D11 adamlu008', mail_content)
"""
print(str(word_list))




json_file_path = os.path.join(os.path.dirname(__file__), '1001S02E09.json')
json_file = open(json_file_path)
json_data = json.load(json_file)

text = ""
for poetry in json_data:
    text += poetry['contents']
word_list = stats_word.stats_text_cn(text, 20)
print(word_list)
"""