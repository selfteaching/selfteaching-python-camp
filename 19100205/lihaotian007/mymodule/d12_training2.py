from wxpy import *
import requests
from pyquery import PyQuery
import stats_word as sw

bot = Bot() #初始化 / 登录

@bot.register([Groups,Friend], SHARING, except_self = False)
def word_frequency(meg) :

    response = requests.get(meg.url) #请求连接，并读取内容

    document = PyQuery(response.text)
    content = document('#js_content').text() #将内容提取出来

    list_a = sw.stats_text(content,100) #对内容进行分词，取其前100个频率的词汇
    a = ''
    for i in range(len(list_a)) :
        a = a + str(list_a[i][0]) + ' ' + str(list_a[i][1]) + ', '
    a = '以上文章的词频统计结果为：' + a
    
    return a


embed()