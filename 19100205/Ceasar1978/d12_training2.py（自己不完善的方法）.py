# 自己摸索出的方法，功能不完善，必须指定好友才能自动回复。

from wxpy import *
bot = Bot()

my_friend = ensure_one(bot.search(u'霁霞'))
#my_friend = bot.friends()


@bot.register()
def print_others(msg):
    print(msg)
    if msg.type == 'Sharing':
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
        str_1 = str(dic) # 将词频统计结果（字典形式）转换成字符串
        print(str_1)
        my_friend.send(str_1)

embed()
