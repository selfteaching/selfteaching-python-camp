#Selfteaching day12 homework ,wechat-practice!！

from mymodule import stats_word as counts  #import module stats_word.py function
import requests
from pyquery import PyQuery
from wxpy import *

#扫码登录微信
bot = Bot() 
#Getting uuid of QR code.
#Downloading QR code.
#Please scan the QR code to log in.
#Please press confirm on your phone.
#Loading the contact, this may take a little while.
#Login successfully as 达达

# 查找朋友:
my_friend=bot.friends().search(sex=MALE,city='广州')[0] #查找好友变量
print（my_friend）
#out[20]: Friend: 罗志全>
    
#自动回复
@bot.register(my_friend)
   def auto_reply_my_friend(msg):
    return 'received:{}({})'.format(msg.text,msg.type)

# 发送文本给好友
my_friend.send('Hello 今天心情不错')
#Out[80]: ↪ 罗志全 : Hello 今天心情不错 (Text) #自动回复


#监听朋友分享的信息
@bot.register(my_friend)
def print_others(msg):
    print(msg) 

#罗志全 : AI，医生，和300万被按下"暂停键"的人 (Sharing)
#罗志全 : 糖果 (Sharing)
#罗志全 : dododo123邀你速学钉钉核心功能，成为首批数字化办公人才 (Sharing)


#接收微信公众号信息，调用Day11程序自动回复统计结果

@bot.register(my_friend,sharing) #接收sharing类信息
def auto_reply(msg):
    sharing_text = requests.get(msg.url) 
    document = PyQuery(sharing_text.text)
    content = document('#js_content').text()
    
    result = counts.stats_text(content,count=100) #统计热词
    return result #将Top100热词自动回复给好友

   

############ day11                               
r=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA') #从微信公众号取内容
r.encoding   #text 格式编码'utf-8'
r.text
response =r.text   #返回文档

from pyquery import PyQuery  #调用网页解释函数
document = PyQuery(response)
text= document('#js_content').text()

from mymodule import stats_word as counts  #import module stats_word.py function

l1=counts.stats_text_cn(text,100) #输出词频TOP 100的词语

stats_string_resut=''.join(str(i)for i in l1) #以字符串输出统计结果 

print('张小龙演讲Top 100高频词',stats_string_resut)# TOP100高频词
                                                              
                                
                                