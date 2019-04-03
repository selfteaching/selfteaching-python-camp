from os import path
import pathlib
import json
import requests
import yagmail
import getpass
path_file = path.dirname(path.realpath(__file__))

# 读取文件


def decoding_json(file_name):
    text = ''
    with open(path_file+'/'+file_name) as f:
        read_data = f.read()
    f.closed

    read_data = json.loads(read_data)

    for item in read_data:
        text += item['contents'] + item['type'] + item['author']
    return text
# print(read_data)

# 获取文章


def request(text):
    r = requests.get(
        text, auth=('user', 'pass'))
    return r.text

# 发送email


def send_email(text):
    sender = input('输入发件人的邮箱:')
    password = getpass.getpass('输入发件人的密码:')
    recipients = input('输入收件人的邮箱:')
    yag = yagmail.SMTP(sender,password,host='smtp.163.com',port='465')
    contents = [text]
    yag.send(recipients, '19100302 macheng2017', contents)



# send_email()