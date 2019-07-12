from mymodule import stats_word

# file = open('/Users/Justco/selfteaching-python-camp/exercises/1901090003/d09/tang300.json','rb')
# text1 = file.read()
# text = text1.decode()

# print(stats_word.stats_text_cn(text,20))

# file.close()

#导入wxpy模块，定义是好友中的SHARING类型
from wxpy import *
bot = Bot()
my_friend = bot.friends()
@bot.register(my_friend,SHARING)

def auto_reply(msg):

#使⽤requests请求信息中的url
    import requests
    response = requests.get(msg.url)

#将response.text用pyquery把链接中内容提取出来
    from pyquery import PyQuery
    document = PyQuery(response.text)
    content = document('#js_content').text()

#使⽤用stats_word中的stats_text对提取结果进⾏行行分析和词频统计处理理(返回前100个词的 统计结果)
    result = str(stats_word.stats_text_cn(content,20))

#开始制作图表部分
    #import matplotlib.pyplot as plt
    import numpy as np
#解决MAC无法正常显示问题    
    import matplotlib.pyplot as plt
    from pylab import mpl
    mpl.rcParams['font.family'] = ['Arial Unicode MS']
    mpl.rcParams['axes.unicode_minus'] =  False
    # 你的原因我终于找到了，我一直没有看到你有下面这句代码，下面这句代码的意思是将上面所有的设置恢复默认，就是你的字体白设置了。
    # plt.rcdefaults()
    fig, ax = plt.subplots()
    result_list=eval(result)
    word=[]
    number=[]
    for i in result_list:
        word.append(i[0])
        number.append(i[1])

    word = tuple(word)
    y_pos = np.arange(len(word))
    number = np.array(number)
    error=np.random.rand(len(word))

    #plt.rcParams['font.sans-serif'] = ['SimHei']         #将中文字体显现
    ax.barh(y_pos,number,xerr=error,align='center',color='red',ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(word)

    ax.invert_yaxis()
    ax.set_xlabel('出现次数') 
    ax.set_title('词频统计表')

    plt.savefig('day13.jpg')
    # plt.savefig('day13.jpg')
    msg.reply_image('day13.jpg')  
embed()    

     




#通过yagmail登录⾃自⼰己的邮箱，将统计结果发送邮件
# import yagmail
# user = input('账号:')
# password = input('密码:')
# smp = 'smtp.qq.com'
# yagmail.SMTP(user=user,password=password,host=smp).send('pythoncamp@163.com', '【1901090003】自学训练营 DAY11 minidv963', str(stats_word.stats_text_cn(content,100)))


