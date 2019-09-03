import matplotlib.pyplot as plt 
import numpy as np 

# np.random.seed(19680801)

plt.rcdefaults()
fig,ax = plt.subplots()

def matplt (xname,ynum):
    plt.rcParams['font.sans-serif']=['SimHei']  #用来正常显示中文标签
    plt.rcParams['font.family']='sans-serif'

    ax.bar(range(len(ynum)), ynum,tick_label=xname)
    ax.set_ylabel('词频')
    ax.set_xlabel('词汇')
    ax.set_title('What frequency of the words in article you sent is?')

    plt.savefig('C:/Users/admin/frcy.png')
    plt.show()

    

from wxpy import *                      #导入模块
bot = Bot()                             #初始化机器人

my_friend = bot.friends().search()         #找到要聊天的好友

@bot.register(my_friend,SHARING)                                #机器人初始化
def friend_sharing(msg):                                #定义这个分析分享内容的函数函数
    link = msg.url                        #获取该消息的地址
    import d11_training1                    #导入昨天的模块
    content=d11_training1.pro_art(link,10)  #这里对昨天的模块进行了分装，把发邮件之外的代码放到了一个函数里
    

    name_list=[]
    num_list=[]
    for x in content:
        name_list.append(x[0])
        num_list.append(x[1])
           

    matplt(name_list,num_list)

    msg.sender.send_image('C:/Users/admin/frcy.png')
    # msg.reply(content)

    # msg.sender.send_image("frcy1.png")
    
    

    


embed()                



