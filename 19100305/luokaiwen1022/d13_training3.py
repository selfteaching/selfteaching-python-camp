import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from wxpy import Bot, Message, embed
import requests
from pyquery import PyQuery
from mymodule import stats_word

'''定义stats函数'''
def stats(url, num):
    try:
        response = requests.get(url)
        # 提取微信公众号正文
        document = PyQuery(response.text)
        print('line 35 ==>', document)#调试用
        content = document('#js_content').text()
        print('line 37 ==>', content)#调试用
        # 统计词频
        statList = stats_word.stats_text(content, num)
        print('line 40 ==>', statList)#调试用
        statString = ''.join(str(i) for i in statList)
        statDict = dict(statList)
        print('line 40 ==>', statDict)#调试用
        return statDict
    except Exception as e:
        print('error ==>', e)

'''定义chartImg'''
cnfont = fm.FontProperties(fname=r"C:\Windows\Fonts\msyh.ttc")
# 定义绘制图标函数并保存为图片
def chartImg(data={}) :
    group_x = list(data.values())
    group_y = list(data.keys())
    fig, ax = plt.subplots()
    ax.barh(group_y,group_x)
    # 自定义表格标签及标题样式
    plt.title('词频统计表',color='black',fontproperties = cnfont,fontsize = 16)
    ax.set_xlabel('数量',fontproperties = cnfont, color = 'grey')
    ax.set_ylabel('词语',fontproperties = cnfont, color = 'grey')
    # 绘制图表
    ax.set_yticklabels(group_y,fontproperties = cnfont)
    
 
    plt.savefig('chart.png')
    return 'chart.png'


# 初始化机器人
bot = Bot()
my_friend = bot.friends()


# 监听分享消息
@bot.register(my_friend)
def get_msg(msg):
    print('line 17 ==>', msg)#调试用
    try:
        if msg.type == 'Sharing':
            print('line 19 ==>', msg.type)#调试用
            retext = stats(msg.url, 5)
            print('line 21 ==>', retext)#调试用
            remsg = chartImg(retext)
            print('line 23 ==>', remsg)#调试用
            msg.reply_image(remsg)
    except Exception as e:
        print('error ==>', e)

embed()

