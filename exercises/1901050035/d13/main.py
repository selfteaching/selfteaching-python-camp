#Selfteaching day13homework ,wxpy -chart practice.3!

from mymodule import stats_word as counts  #import module stats_word.py function
import requests
from pyquery import PyQuery
from wxpy import *   
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


#扫码登录微信
bot = Bot() 

# 查找朋友:
my_friend=bot.friends().search(sex=MALE,city='广州')[0] #查找好友变量
print（my_friend）

    
#自动回复
@bot.register(my_friend)
def auto_reply_my_friend(msg):
   return 'received:{}({})'.format(msg.text,msg.type)

# 发送文本和图片给好友
my_friend.send('Hello 今天心情不错')
my_friend.send_image('top_n.png')   #发送统计结果图片


#监听朋友信息
@bot.register(my_friend)
def print_others(msg):
    print(msg) 

#监听朋友分享的信息,自动回复统计数据和图表
@bot.register(my_friend,SHARING) #接收sharing类信息
def auto_reply(msg):
    sharing_text = requests.get(msg.url)  
    document = PyQuery(sharing_text.text)
    content = document('#js_content').text()

    import numpy as np                         #调用numpy 库函数
    import matplotlib.pyplot as plt             #调用matplotlib 库函数
    from matplotlib.ticker import FuncFormatter
    
    l1=counts.stats_text_cn(content,count=20)      ##统计微信消息前10位热词
    data=dict(l1)                                  #将统计结果热词数据字典化
    group_data = list(data.values())
    group_names = list(data.keys())
    group_mean = np.mean(group_data)

    plt.rcParams['font.sans-serif']=['SimHei']     # 统计表格数据格式汉化

    fig, ax = plt.subplots(figsize=(8, 8))          #使用plt模版导入数据生成图表
    ax.barh(group_names, group_data)
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment='right')
    ax.set(xlim=[0, 30], xlabel='词频( 次 )', ylabel=' 热词 ',title='TOP N 热词')
    plt.show()
    fig.savefig('top_n.png', transparent=False, dpi=80, bbox_inches="tight")  # 将统计图表存成png格式
    
    my_friend.send_image('top_n.png')   #发送统计结果图片
    result = l1 #统计热词

    return result #将Top n 热词自动回复给好友 


########################################################################

#接收微信公众号信息，调用Day11程序自动回复统计结果

@bot.register(my_friend,SHARING) #接收sharing类信息
def auto_reply(msg):
    sharing_text = requests.get(msg.url) 
    document = PyQuery(sharing_text.text)
    content = document('#js_content').text()
    
    result = counts.stats_text(content,count=100) #统计热词
    return result #将Top100热词自动回复给好友

import requests #调用requests 函数
r=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA') #从微信公众号取内容
r.encoding   #text 格式编码'utf-8'
r.text
response =r.text   #返回文档

from pyquery import PyQuery  #调用网页解释函数
document = PyQuery(response)
text = document('#js_content').text()

from mymodule import stats_word as counts  #import module stats_word.py function

l1=counts.stats_text_cn(text,100) #输出词频TOP 100的词语

stats_string_resut=''.join(str(i)for i in l1) #以字符串输出统计结果 
print('张小龙演讲Top 100高频词',stats_string_resut)

