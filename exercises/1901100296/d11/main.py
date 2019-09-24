from mymodule import stats_word
import getpass
import yagmail

def postemail(content,title):
    sender = input('输⼊发件⼈邮箱:')
    password = getpass.getpass('输⼊发件⼈邮箱密码(可复制粘贴):') 
    recipients = input('输⼊收件⼈邮箱:')
    yag = yagmail.SMTP(sender,password)
    yag.send(recipients,title,content)

if __name__ == '__main__':
    url='https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'
    content = stats_word.stats_text_cn(stats_word.getcontent(url),100)
    # print('统计结果：',content)
    postemail(content,'统计结果')

