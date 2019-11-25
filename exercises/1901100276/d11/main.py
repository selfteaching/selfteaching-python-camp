from mymodule import stats_word
import  yagmail
import  requests
import pyquery
import getpass
try:
        r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')#请求链接，获取返回结果

        from pyquery import PyQuery     #提取正⽂

        document = PyQuery(r.text)

        content= document('#js_content').text()
    
        result = stats_word.stats_text(content,100)     #返回前 100 个词的统计结果
        result= str(result)     #转换成 str 类型
        print(result)
        sender = input('输⼊发件⼈邮箱:')
        password = getpass.getpass('输⼊发件⼈邮箱密码:')
        recipients = input('输⼊收件⼈邮箱:')

        yag = yagmail.SMTP(user = sender, password = password, host = 'smtp.qq.com')
        yag.send(recipients, '[1901100276]+自学训练营学习20群+zerasq', contents=result)
except ValueError:
        print('错误，非字符串')