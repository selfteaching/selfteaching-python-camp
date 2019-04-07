# day13 20190405-- copied from @wangrui0802 @wengyadong @ss412231878
#question: if my d12 file is not in the same level of files used today, will there be bugged?
#my plan A is to input all the codes included in d12

#from mymodule import stats_word as sw
#import requests
#from pyquery import PyQuery
##from wxpy import * error notification resolved by issue #1169
#from wxpy import Bot,Message,embed


#def main():
#    bot = Bot(cache_path=True)#扫描二维码登陆微信 #issue1195 avoiding scanning again shortly
#    my_friend = bot.friends()#回复对象为所有好友
#    @bot.register(my_friend)
#    @bot.register(msg_types='Sharing')#监听好友分享的消息 why 'Sharing'expression? SHARING got errors why oh why? input distinguish problems again?
#    def auto_reply(msg):
#        response = requests.get(msg.url)#msg.url为分享的网址
#        document = PyQuery(response.text)
#        content = document('#js_content').text()
#        #像d11一样处理文本
#        result = sw.stats_text_cn(content,count=100)
#        wechat_word = ''.join(str(i)for i in result) # seems better str this type in case causing trouble in reading
#        return wechat_word#将结果返回给好友

#    embed()#d堵塞线程，保持监听

#if __name__=='__main__':
#    main()
##I am not so sure but feel this should not be the same as day 12, thus I wanna try some revision below day13's codes:

# day13 20190405-- copied from @wangrui0802(101) @wengyadong(102) @ss412231878(205) @slona-song(105)
# with Cat's thoughts and queries listed for further exploration later. try as hard as you could for now...
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
# np.random.seed(19680801)
#### 105 @slona-song found through issue#1284 and her codes revealed her thoughts clearly and need to be explored !!! a golden mine 

plt.rcdefaults()
fig,ax = plt.subplots()
# 设置中文字体  # issue#1692 provided another solution on font setting problems pyplotz: pip install
cnfont = fm.FontProperties(fname='/Users/cat/Library/Fonts/SimHei.ttf')

# 定义绘制图标函数并保存为图片
def chartImg(data={}) :
    group_x = list(data.values())
    group_y = list(data.keys())
    # 自定义表格标签及标题样式
    plt.title('词频统计表',color='black',fontproperties = cnfont,fontsize = 16) #ax.set_title ? copied @slona-song's code a
    ax.set_xlabel('数量',fontproperties = cnfont, color = 'grey')
    ax.set_ylabel('词语',fontproperties = cnfont, color = 'grey')
    # 绘制图表
    ax.set_yticklabels(group_y,fontproperties = cnfont)
    ax.barh(group_y,group_x)
    # 保存绘制文件
    plt.savefig('chart.png')
    return 'chart.png'


from mymodule import stats_word as sw
import requests
from pyquery import PyQuery
#from wxpy import * error notification resolved by issue #1169
from wxpy import Bot,Message,embed


def main():
    bot = Bot(cache_path=True)#扫描二维码登陆微信 #issue1195 avoiding scanning again shortly
    my_friend = bot.friends()#回复对象为所有好友
    @bot.register(my_friend)
    @bot.register(msg_types='Sharing')#监听好友分享的消息 why 'Sharing'expression? SHARING got errors why oh why? input distinguish problems again?
    
    def reply_my_friend(msg):
         
        wechat = requests.get(msg.url)
        document = PyQuery(wechat.text)
        content = document('#js_content').text()
#        result = sw.stats_text_cn(content,count=100)
#        wechat_word = ''.join(str(i)for i in result) # seems better str this type in case causing trouble in reading
#        return
        list_a = sw.stats_text_cn(content,100)#接收发来的分享链接的文字，并处理成词频统计结果
           
        msg.reply_image(chartImg(list_a)) #回复刚才保存的图片给好友        
        return

    embed()#让程序执行到这里后返回，以便于重新执行

if __name__=='__main__':#这条语句能够帮助windows正常系统执行上面部分代码
    main()