
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from wxpy import Bot, Message, embed
import requests
from pyquery import PyQuery
from mymodule import stats_word

# 初始化机器人
bot = Bot()
my_friend = bot.friends()

# 监听分享消息
@bot.register(my_friend)
def get_msg(msg):
    if msg.type == 'Sharing':
        retext = stats(msg.url, 5)
        remsg = chartImg(retext)
        msg.reply_image(remsg)
    else:
        pass

embed()

'''定义stats函数'''
def stats(url, num):
    response = requests.get(url)
    # 提取微信公众号正文
    document = PyQuery(response.text)
    content = document('#js_content').text()
    # 统计词频
    statList = stats_word.stats_text(content, num)
#    statString = ''.join(str(i) for i in statList)
    statDict = dict(statList)
    return statDict

'''定义chartImg'''
cnfont = fm.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')
# 定义绘制图标函数并保存为图片
def chartImg(data={}):
    group_x = list(data.values())
    group_y = list(data.keys())
    fig, ax = plt.subplots()
    # 自定义表格标签及标题样式
    plt.title('词频统计表', color='black', fontproperties=cnfont, fontsize=16)
    ax.set_xlabel('数量', fontproperties=cnfont, color='grey')
    ax.set_ylabel('词语', fontproperties=cnfont, color='grey')
    # 绘制图表
    ax.set_yticklabels(group_y, fontproperties=cnfont)
    ax.barh(group_y, group_x)
    # 保存绘制文件
    plt.savefig('chart.png')
    return 'chart.png'
