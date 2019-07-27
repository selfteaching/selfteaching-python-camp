＃初始化机器人
bot = Bot（）
my_friend = bot.friends（）

＃监听分享消息，并回复分析结果
@ bot.register（my_friend）
def  get_msg（msg）：
    if msg.type ==  ' Sharing '：
        retext = st.stats（msg.url，5）
        remsg = fg.chartImg（retext）
        msg.reply_image（remsg）
    否则：
        通过
嵌入（）