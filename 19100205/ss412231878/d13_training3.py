#from wxpy import *
#from pyquery import PyQuery
#import requests
#from mymodule import stats_word
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import random as rd


#生成图片
def counter_stats(list_a):
    word = []
    number = []
    for i in list_a:
        word.append(i[0])
        number.append(i[1]) 
    #print (word)
    #print(number)

    plt.rcdefaults()
    fig,ax = plt.subplots()

    counter = word
    y_counter = np.arange(len(counter))
    counter_number = np.array(number)

    mpl.rcParams['font.sans-serif'] = ['SimHei']   #设置简黑字体
    mpl.rcParams['axes.unicode_minus'] = False
    ax.barh(y_counter,counter_number,align='center',color='pink',ecolor='black')
    ax.set_yticks(y_counter)
    ax.set_yticklabels(counter)
    ax.invert_yaxis()
    ax.set_xlabel('Counter')
    ax.set_title('Counter_stats_word')

    #plt.show()
    path = 'C:\\Users\\33\\' + str(rd.randint(1,100)) + '.png'
    print(path)
    plt.savefig(path)
    return path

#word = ['吴千语', '出演', '施伯雄', '自己', '新闻', '恋情', '希望', '时候', '黄百鸣', '喜剧电影']
#number = [24, 7, 6, 5, 5, 4, 4, 4, 4, 4]
#p = counter_stats(word,number) 

#def main():#这里与最后的命名保持一致
#    bot = Bot()#登录微信的命令
#    my_friend = bot.friends()#发给所有好友

#    @bot.register(msg_types=SHARING)#接收分享类信息
#    def reply_my_friend(msg):#设置返回day11一样的词频统计
#        if msg.type == "Sharing":
#            word = []
#            number = []

#            wechat = requests.get(msg.url)
#            document = PyQuery(wechat.text)
#            content = document('#js_content').text()
#            wx = stats_word.stats_text(content)
#            wechat_word = ''.join(str(i) for i in wx) 
#            for i in wx:
#                word.append(i[0])
#                number.append(i[1]) 
#            print (word)
#            print(number)

#            p = counter_stats(word,number)            
#            my_friend.send(msg)
#            my_friend.send(wx)
#            my_friend.send_image('counter_stats.jpg')

#    embed()#让程序执行到这里后返回，以便于重新执行





#if __name__=='__main__':#这条语句能够帮助windows正常系统执行上面部分代码
#    main()