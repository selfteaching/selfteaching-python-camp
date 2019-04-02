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
    dic = mymodule.stats_word.stats_text_cn(content,5) # 调用函数进行分词并统计词频
    
    dic = dict(dic)
    from pylab import mpl  

    mpl.rcParams['font.sans-serif'] = ['SimHei'] 
    import matplotlib.pyplot
    import numpy
    #matplotlib.pyplot.rcParams['font.sans-serif']=['SimHei']
    #matplotlib.pyplot.rcParams['axes.unicode_minus'] = False
    
    # Fixing random state for reproducibility
    numpy.random.seed(19680801)


    matplotlib.pyplot.rcdefaults()
    fig, ax = matplotlib.pyplot.subplots()

    # Example data
    word = []
    frequency = []
    for i in dic:
        word.append(i)
        frequency.append(dic[i])

    y_pos = numpy.arange(len(word))

    error = numpy.random.rand(len(word))

    ax.barh(y_pos, frequency, xerr=error, align='center',
            color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(word)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('词语出现次数')
    ax.set_title('words_frequency')

    matplotlib.pyplot.savefig('words_frequency.png')
    msg.reply_image('words_frequency.png')
embed()




    