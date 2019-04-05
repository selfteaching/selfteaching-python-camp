import re                   #导入正则表达式
import collections          #导入计数集合，还可以像导入文档分析库一样导入
import jieba                #导入jieba三方库
import requests             #导入网络请求三方库
from pyquery import PyQuery #从文档分析库导入文档分析函数
#import yagmail              #导入邮箱库
'''
import getpass
sender = input('输入发件人邮箱:')
password = getpass.getpass('输入发件人邮箱密码:')
recipients = input('输入收件人邮箱:')


r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')    #请求网页链接内容
doc = PyQuery(r.text)        #请求网络返回文档后，进行文档分析
content = doc('#js_content').text()   #提取文本内容
'''

from wxpy import *           #导入微信机器人
bot = Bot()                  #机器人初始化

my_friend = bot.friends()    #微信全部好友都提取出来

@bot.register(my_friend)     #注册函数
def SHARING_Msg(msg):
        if msg.type == 'Sharing':     #这个类型这里，首字母必须要大写，这个细节要注意
                response = requests.get(msg.url)    #请求网络
                document = PyQuery(response.text)    #解析文档
                content = document('#js_content').text()    #提取内容
                          
                words = ''.join(re.findall(r'[\u4e00-\u9fa5]',content))   #运用正则表达式提取汉字
                list0 = jieba.cut(words) #用‘结巴’分词                       
                c = collections.Counter() #新建空统计列表         
                for x in list0:           #利用循环和分支进词语长度大于等于2的词频统计
                        if len(x) > 1:
                                c[x] += 1
                #num = int(input("您想统计前多少个词频最高词语："))  #交互式按需统计
                str0 = str(dict(c.most_common(100)))  #强制转换成列表
                msg.reply(str0)
        else:
                msg.reply("我是可爱的文本词频统计机器人，请把你的链接发给我吧")
                print(msg.sender.name,':',msg.text,'Msg Type:',msg.type)
embed()

'''
yag = yagmail.SMTP(sender,password,'smtp.qq.com') #使用QQ的SMTP服务服务器
yag.send(recipients,'19100304 baichampion',str0)
'''