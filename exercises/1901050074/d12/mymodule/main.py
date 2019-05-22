import requests # 网络请求库
from pyquery import PyQuery # 文档解析库
from stats_word import stats_text_cn    # 统计中文词频
from wxpy import *

def main():
    bot=Bot()   #扫描二维码登录微信
    my_friend=bot.friends() #设置回复对象为所有好友

    @bot.register(my_friend,SHARING)    #接受分享类消息
    def auto_reply(msg):
        response=requests.get(msg.url)  #获取分享的网址
    # 提取微信公众号正文伪代码
        document = PyQuery(response.text) 
        content = document('#js_content').text()

        # 统计前100个中文词频
        try:
            result=str(stats_text_cn(content,count=100))
            return(result)  #将结果返回给好友
        except ValueError as e:
            print('ValueError:',e)

    embed()

if __name__=='__main__':
    main()