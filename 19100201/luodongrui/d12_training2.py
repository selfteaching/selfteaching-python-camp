# 导入模块
import wxpy
from pyquery import PyQuery
import requests
import stats_word
# 初始化机器人，扫码登陆
bot = Bot()

# 监听好友消息
@bot.register(my_friend)
def get_msg (msg):  
# 如果消息为 分享(SHARING)类型，则获取消息的网页链接(msg.ugl)
    if msg.type == 'Sharing' :
        target_url = msg.url
        stats_msg = d12_training1.stats(target_url)
# 将获取的链接使用 实战项目1中的方式进行处理
url = target_url 
response = requests.get(url)
document = PyQuery(response.text) 
content = document('#js_content').text()
string = ','.join(str(i) for i in stats_word.stats_text_cn(content))
# 将处理结果返回给发送消息过来的好友
my_friend.send(stats_msg)
