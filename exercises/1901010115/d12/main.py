from mymodule import stats_word #读取模块
import json #引入jsan解码库
import jieba

import requests #引入requests库用于获取网页HTML信息

from pyquery import PyQuery as pq #引入pyquery库解析获取的HTML信息

from wxpy import * #引入wxpy模块
bot = Bot(cache_path=True) #初始化wxpy，扫码登录
my_friend = bot.friends() #搜索好友信息
@bot.register(my_friend,SHARING) #注册消息接收器（并限定为来自好友的，分享类信息）
def my_friend_sharing(msg): #定义函数 ，当有msg发送过来，则用requests模块获取该网址
    msg_sharing = requests.get('msg.url') #这里就是获取msg的网址信息了
    doc = pq(msg_sharing.text) #解析HTML代码
    msg_content = doc('#js_content').text() #提取文本
    msg_result = stats_word.cn(meg_content,100) #引用模块统计处理文本
    msg_result_str = str(msg_result) #返回信息处理结果
    my_friend.send(msg_result_str) #向好友发送该结果
#以上函数没有使用return等结构我没太看懂，应该是@装饰器的使用与一般的函数不一样，得查询清楚
embed() #堵塞线程。确保Terminal在运行完以上函数后，仍能在线接受新信息



#本次作业由于微信改版的原因，wxpy库不能正常运行，一直报错'pass ticket'。所以以上代码是未经测试的，回头阅读完装饰器内容后，找机会回来做测试。