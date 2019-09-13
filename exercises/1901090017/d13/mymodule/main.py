import requests                 #获取网址
import stats_word #统计单词
from wxpy import *  #引⼊ wxpy 模块 (微信机器人)
from pyquery import PyQuery as py   #生成文本.txt
import matplotlib.pyplot as plt #绘制直方图


bot = Bot(console_qr=True, cache_path=True) # 初始化机器人，扫码登陆
my_friend = bot.friends()
@bot.register(my_friend,SHARING)
def reply_my_friend(msg):
    response = requests.get(msg.url)
    document = py(response.text) 
    content = document('#js_content').text()
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

 
 