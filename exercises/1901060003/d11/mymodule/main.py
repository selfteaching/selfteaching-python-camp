import stats_word
from os import path
import json
import re
import logging
import requests
import yagmail
from pyquery import PyQuery
url="https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA"
r=requests.get(url)
document=PyQuery(r.text)
content=document('#js_content').text()
# print(content)
print(type(content))



# logging.basicConfig(
#     format='file:%(filename)s line:%(lineno)d message: %(message)s', level=logging.DEBUG)


# def load_file():
#     '''
#     1.
#     下面是常用的获取文件路径的方式，要确保 tang300.json 跟当前文件在同一文件夹下，这两种方式等价
#     file_path = path.join(path.dirname(path.abspath(__file__)), './tang300.json')
#     '''
#     file_path = path.join(path.dirname(path.abspath(__file__)), 'tang300.json')
#     print('当前文件路径：', __file__, '\n读取文件路径：', file_path)

#     '''

#     2.
#     这种方式表示 tang300.json 在当前文件的上一级目录
#     file_path = path.join(path.dirname(path.abspath(__file__)), '../tang300.json')
#     print(__file__, file_path)

#     3.
#     这种方式表示 tang300.json 在当前文件的上一级目录的 data 文件夹下
#     file_path = path.join(path.dirname(path.abspath(__file__)), '../data/tang300.json')
#     print(__file__, file_path)
#     '''

#     with open(file_path, 'r', encoding='utf-8') as f:
#         return f.read()


# def merge_poems(data):
#     poems = ''
#     for item in data:
#         poems += item.get('contents', '')
#     return poems


def main():
    s=stats_word.stats_text(content, 100)    
    print(type(s))
    newtype=str(s)
    type(newtype)
    print(type(s))
    print(s)
    import getpass
    sender = input('输入发件人邮箱：')
    password = getpass.getpass('输⼊发件⼈邮箱密码(可复制粘贴):')
    recipients = input('输入收件人邮箱:')
    yag=yagmail.SMTP(sender,password,'smtp.qq.com')
    yag.send(recipients,'自学训练营学习5群 Day11 williswill',str(s))

    # 自学训练营学习5群 Day11 williswill
    # 结果如下：
    print(s)
    # try:
    #     data = load_file()
    #     #logging.info(data[0])
    #     poems = merge_poems(json.loads(data))
    #     logging.info('result ==> %s', stats_word.stats_text_cn(poems, 100))
    # except Exception as e:
    #     logging.exception(e)



if __name__ == "__main__":
    main()