""" 
当程序使用“＠函数A”装饰另一个函数B时，实际上完成如下两步：
将被修饰的函数B作为参数传给 ＠函数 A。
将函数 B 替换（装饰）成第 1 步的返回值。
所谓的装饰器，就是通过装饰器函数，来修改原函数的一些功能，使得原函数不需要修改。
"""
import requests                 #获取网址
import stats_word #统计单词
from wxpy import *  #引⼊ wxpy 模块 (微信机器人)
from pyquery import PyQuery as py 

bot = Bot(console_qr=True, cache_path=True) # 初始化机器人，扫码登陆
my_friend = bot.friends()
@bot.register(my_friend,SHARING)
def auto_get_url(msg):
    response = requests.get(msg.url)
    document = py(response.text) 
    content = document('#js_content').text()
    text1 = stats_word.stats_text_cn(content,100)
    text2 = str(text1)
    bot.file_helper.send(text1)
    return text2

# 堵塞线程，并进入 Python 命令行
embed()
 
 