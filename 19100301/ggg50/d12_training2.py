# day_12
# 1.把上次作业完成的处理微信文章url，提取内容，转化内容封装到一个函数里面，
#   输入 url（注意，这个 url只能是微信文章的 url) 就可以得到全文词频前一
#   百的词汇
# 2.安装、调用 wxpy。



import requests
from os import path
from pyquery import PyQuery
from mymodule import stats_word_day10
from wxpy import *

# input a weixin's article url, and then return a sorted word dict.
def sort_text(url):
    response = requests.get(url)
    document = PyQuery(response.text)
    r_content = document('#js_content').text()

    # input text and define output word numbers
    return stats_word_day10.stats_text_cn(r_content, 100)

bot = Bot()

@bot.register()
def print_others(msg):
    # if the message type is "Sharing", assigning the message sender property to my_friend, 
    # and then senting the sorted dict to "my_friend"
    if msg.type == "Sharing":
        my_friend = msg.sender
        my_friend.send(sort_text(msg.url))

embed()


