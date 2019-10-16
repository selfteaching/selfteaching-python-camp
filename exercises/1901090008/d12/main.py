import wxpy                                                            # 导入wxpy模块，from wxpy import *,会报错函数不可用，方法1：*改成以下代码的所用到的所有函数，方法2：在以下所用到的wxpy函数前加上wxpy.

bot = wxpy.Bot()                                                       # 扫码登陆微信 

my_friend= bot.friends().search('云如', city='抚州')[0]                 #搜索朋友       
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
    results= s.stats_text_cn(content,100)                               #调用函数，统计词频
    r_string= ''.join(str(i)for i in results)                           #列表转化为字符串
    print(r_string) 
    return r_string                                                     #自动把结果回复的朋友 return=msg.reply()

wxpy.embed()                                                            #堵塞线程，以保持监听状态 