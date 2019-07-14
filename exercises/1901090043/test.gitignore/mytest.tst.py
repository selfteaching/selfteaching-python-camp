# coding:utf-8  
import json
import requests
from wxpy import *
 
def auto_ai(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key="34c5badc793a43c284faa18b62c52c00"
    payload={
        "key":api_key,
        "info":text,
        "userid":"666"
        }
    r = requests.post(url,data=json.dumps(payload))
    result = json.loads(r.content)
    if ('url' in result.keys()):
        return result["text"]+result["url"]
    else:
        return result["text"]
 
 
bot = Bot(cache_path=True)#登录缓存
#bot.file_helper.send('[奸笑][奸笑]')
print('姜翔AI已经启动')

# 回复 my_friend 的消息 (优先匹配后注册的函数!)
#my_friend = bot.friends().search("么么哒")[0]
# 发送文本给好友
#my_friend.send('在吗？回复下！')

boring_group1 = bot.groups().search('大鄱阳')[0]

print(boring_group1.owner)
i = 0
for items in boring_group1:
   i += 1
print('成员数量为：',i)

#boring_group1.remove_members(boring_group1.owner,'王仁林')
boring_group1.search('菲儿')[0].remove()
#print(boring_group1.search('菲儿')[0])
#print(boring_group1.search())
#print('熊猫已经被移出群！')
#boring_group1.add_members('么么哒')

i = 0
for items in boring_group1:
   i += 1
print('成员数量为：',i)
#i = 0
#for items in bot.chats(update=False):
#    i += 1

#print('一共有好友:',i)

#print(boring_group1.search(keywords=None))

@bot.register(boring_group1)
def group_message(msg):

    print('[接收]'+str(msg))
    if (msg.type!='Text'):
        ret = '[奸笑][奸笑]'
    else:
        ret = auto_ai(msg.text)
        print('[发送]'+str(ret))
    
    return ret
 
@bot.register(chats = [Friend])
def forward_message(msg):
    print('[接收]'+str(msg))
    if (msg.type!='Text'):
        ret = '[奸笑][奸笑]'
        print(msg.url)
    else:
        ret = auto_ai(msg.text)
        print('[发送]'+str(ret))
    return ret
 
embed()