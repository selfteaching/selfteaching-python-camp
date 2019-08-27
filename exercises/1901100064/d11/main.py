from mymodule import stats_word
from os import path
import re
import yagmail
import keyring
import getpass

sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱密码（可复制粘贴）：')
recipients =input('输入收件人邮箱：')

yagmail.register(sender,password)

yag = yagmail.SMTP('lishuaizzu@163.com')
contents = ['This is the body', '/local/path/song.mp3']

yag.send('lishuaizzu@163.com', 'subject', contents)
