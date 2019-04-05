
from wxpy import *
bot = Bot()
my_friend = bot.friends()
@bot.register(my_friend,SHARING)
def auto_reply(msg):

    text = msg.url
    print(text)

    import requests
    response = requests.get(text) 
    # 以上通过requests请求文章链接，获取网页内容


    from pyquery import PyQuery
    document = PyQuery(response.text)
    content = document('#js_content').text() # 将网页内容提取为一个字符串文本作为输入

    print(content)


    import mymodule.stats_word


    try:
        if not isinstance(content,str):
            raise ValueError()
        
    except ValueError:
        print('输入的不是文本格式，请重新输入：')   
    dic = mymodule.stats_word.stats_text_cn(content) # 调用函数进行分词并统计词频
    
    dic = dict(dic) # counter函数输出的结果是一个二维list，而非字典，此步操作将二维list转换为字典。

    # 以下是通过matplotlib和numpy库将词频分析结果进行图形化
    import matplotlib.pyplot as plt
    import numpy as ny
    
    
    # Fixing random state for reproducibility
    ny.random.seed(19680801)


    plt.rcdefaults()
    fig, ax = plt.subplots()

    # Example data
    word = []
    frequency = []
    for i in dic:
        word.append(i)
        frequency.append(dic[i]) #将词频统计结果字典拆分成两个列表，一个包含词语，一个包含出现的次数

    y_pos = ny.arange(len(word))

    error = ny.random.rand(len(word))
    plt.rcParams['font.sans-serif'] = ['SimHei'] #这一步是为了添加字体，否则汉字会显示为方框

    ax.barh(y_pos, frequency, xerr=error, align='center',
            color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(word)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('词语出现次数')
    ax.set_title('词频统计')

    plt.savefig('words_frequency.png') # 将结果保存为图片文件
    msg.reply_image('words_frequency.png') # 将图片发送给好友
embed()

