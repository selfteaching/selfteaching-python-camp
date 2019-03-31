
导入请求
来自 wxpy import  * 
bot = Bot（login_callback =  True）

my_friend = bot.friends（）。search（'peer'）

@ bot.register（）               ＃打印来自好友的消息
def  print_other（msg）：
    打印（msg）

@ bot.register（my_friend）          ＃回复my_friend的消息
def  reply_my_friend（msg）：
    返回 '接收的：{} （{} ）' .format（msg.text，msg.type）

@ bot.register（msg_types = SHARING）＃监听好友分享的消息
def  main（）：
    my_friend.send（'请分享一篇公众号链接给我）
    response = requests.get（' msg.url '）
    来自 pyquery 导入 PyQuery
    document = PyQuery（response.text）        ＃将内容抓取下来
    content = document（' ＃ js_content '）。 text（）       ＃获取正文内容
    import stats_word_d11
    s = stats_word_d11.stats_text（content，100）         ＃引用stats.text来统计100个词
    s =  str（s）
    print（s）                                        ＃转为字符串str类型
    my_friend.send（S）
    embed（）                                     ＃ d堵塞线程，保持监听
如果 __name__ == ' __main__ '：
        主要（）