from mymodule import stats_word
import traceback
import logging
import json
from os import path
import yagmail
from pyquery import PyQuery
import requests
import getpass

def test_traceback():
  try:
    stats_word.stats_text(text)
  except Exception as e:
    print("trace_back==>",e)
    print(traceback.format_exc())
def test_logger():
  try:
    stats_word.stats_text(text)
  except Exception as e:
    logging.exception(e)


def load_file():
  
  file_path = path.join(path.dirname(path.abspath(__file__)),'tang300.json')
  print("当前文件路径==>",__file__,'\n读取文件路径==>',file_path)
  '''
  tang300.json在上一级目录
  file_path = path.join(path.dirname(path.abspath(__file__)),'../tang300.json')

  tang300.json文件在上一级目录的data目录下的文件
  file_path = path.join(path.dirname(path.abspath(__file__)),'../data/tang300.json')
  '''

  with open(file_path,'r',encoding='utf-8') as f:
    return f.read()
  
#data为由json转换而来的字典
def merge_poems(data):
  poems = ''
  for item in data:
    poems +=item.get('contents','')
  return poems

def read_page(url):
  response = requests.get(url)
#  print(response.headers['content-type'])
  document = PyQuery(response.text)
  content = document('#js_content').text()
  return stats_word.stats_text_cn(content,100)
def send_mail(content):
  username = input('请输入邮件账号：')
  passwd = input('请输入授权码:')
  mail = yagmail.SMTP(user=username,
                      password=passwd,
                      host='smtp.163.com',
                      # smtp_ssl=True
                      ) #如果用的是qq邮箱或者你们公司的邮箱使用是安全协议的话，必须写上 smtp_ssl=True
  mail.send(
      to='pythoncamp@163.com', #如果多个收件人的话，写成list.
      cc='13910255158@163.com',#抄送
      subject='张小龙',#邮件标题
      contents = content)#邮件正文
  #      attachments=[r'C:\Users\Desktop\a.txt',
  #                  r'C:\pp\b.txt'])#附件如果只有一个的话，用字符串就行，attachments=r'C:\\pp\\b.txt'

  
def main():
  try:
    data = load_file()
    logging.info(data[0])
    poems = merge_poems(json.loads(data))

    logging.info('result ==> %s',stats_word.stats_text_cn(poems,100))
    print(stats_word.stats_text_cn(poems,20))
  except Exception as e:
    logging.exception(e)


if __name__ == '__main__':
#  test_traceback()
#  test_logger()
#  print(stats_word.stats_text(text))
#  main()
  url = 'https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'
  contents = json.dumps(dict(read_page(url)),ensure_ascii=False)
  send_mail(contents)

