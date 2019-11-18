# 先导入第三方库
import yagmail, requests, pyquery, getpass, csv
from pyquery import PyQuery
from  mymodule import stats_word
import matplotlib.pyplot as plt
import numpy as np
from wxpy import *

# 初始化机器人，扫码登陆
bot = Bot()
# 搜索名称含有 "三月" 的男性合肥好友
my_friend = bot.friends().search('三月', sex=MALE, city="合肥")[0]
# 发送文本给好友
my_friend.send('分享任意微信文章给我')
# 回复 my_friend 的消息
@bot.register(my_friend)
def reply_my_friend(msg):
    if msg.type == 'Sharing':
        response = requests.get(msg.url) # 获取该网页内容
        document = PyQuery(response.text) 
        content = document('#js_content').text() # 将网页内容转换成文本
        word_dict = dict(stats_word.stats_text_cn(content, 10))
        # 作图
        plt.rcParams['font.sans-serif']=['SimHei']            # 显示中文字体
        word_data = []
        for key, value in word_dict.items():                    # 遍历字典
            word_data.append([value, key])                      # 添加数据
        for i in range(0, 10):
            plt.bar((word_data[i][1],),(word_data[i][0],), facecolor='#9999ff', edgecolor='white')
        plt.title('中文词频(TOP1-10)')     # 显示标题
        plt.xlabel('中文词汇')             # 显示x轴名称
        plt.ylabel('词频')                 # 显示y轴名称
        plt.legend('直方图')               # 显示图例
        plt.savefig('word_dict.png', dpi=300) # 保存图片
        msg.reply_image('word_dict.png') # 微信返回图片

embed()
