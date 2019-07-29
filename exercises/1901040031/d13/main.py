
import wxpy                                                            # 导入wxpy模块，from wxpy import *,会报错函数不可用，方法1：*改成以下代码的所用到的所有函数，方法2：在以下所用到的wxpy函数前加上wxpy.

bot = wxpy.Bot()                                                       # 扫码登陆微信 

my_friend= bot.friends().search('云如',province='江西')[0]              #搜索朋友       
my_friend.send('请给我分享一篇文章可好')                                 #请求朋友发送消息
SHARING= 'Sharing'                                                     #消息类型
@bot.register(my_friend, SHARING)                                      #装饰器，预先注册：预先将特定聊天对象，特定类型消息，注册到对应的处理函数，实现自动回复
def print_msg(msg):                                                    
    import requests
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #禁用安全证书，解决InsecureRequestWarning
    response = requests.get(msg.url)                                    #msg.url获取朋友分享类消息的网址
    from pyquery import PyQuery
    document = PyQuery(response.text)
    content =document('#js_content').text()                             #从网页中导出文本
    from mymodule import stats_word as s 
    dic = s.stats_text_cn(content,20)                               #调用函数，统计词频
    dic = dict(dic)
    

    import matplotlib.pyplot as plt                                  #导入matplotlib作图
    import numpy as np
    # from  pylib  import mpl                                        解决中文乱码的问题，因为matplotlib中没有中文字体的相关信息 ，动态设置matplotlibrc参数
    #mpl.rcParams['font.sans-serif'] = ['FangSong']                  #指定默认字体，如何改变字体大小
    #mpl.rcParams['axes.unicode_minus'] = False                      #解决保存图像是负号'-'显示为方块的问题,此方法行不通
    
    from matplotlib.font_manager import FontProperties               #解决中文乱码，使用字体管理器

    
    
    plt.rcdefaults()
    fig, ax = plt.subplots()                                         #创建一个图形和一组子图

    words = []
    frequency = []
    for i in dic:                                                    #遍历字典
        words.append(i)                                              #提取字典中词组
        frequency.append(dic[i])                                     #提取字典中的数值
    
    y_pos = np.arange(len(words))                                    #在给定间隔内返回均匀间隔的值


    ax.barh(y_pos, frequency , align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(words,fontproperties = 'SimHei')
    ax.invert_yaxis()                                                #标签顺序从上到下 
    ax.set_xlabel(u'出现次数',fontproperties = 'SimHei')              #注意在中文字符串前加上u
    ax.set_title(u'分享文章的词频统计 ',fontproperties='SimHei')
    
    
    plt.savefig('chart.png')                                            
    msg.reply_image("chart.png")    
                                       
wxpy.embed()      #堵塞线程，以保持监听状态