import re                   #导入正则表达式
import collections          #导入计数集合，还可以像导入文档分析库一样导入
import jieba                #导入jieba三方库
import requests             #导入网络请求三方库
from pyquery import PyQuery #从文档分析库导入文档分析函数
#import yagmail              #导入邮箱库
import matplotlib.pyplot as plt   #导入2D绘图库
import numpy as np        #导入科学计算库
import matplotlib         #导入这个包用于显示汉字

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
                Reply = dict(c.most_common(10))
                num_tuple = tuple(Reply.values())#转换成元组出现次数
                name_tuple = tuple(Reply.keys())#转换成元组词语
                matplotlib.rcParams['font.family'] = 'SimHei'     #在rc语句中改成中文

                count = 10             #横轴显示数量
                bar_width = 0.35       #词频柱宽度
                opacity = 0.4          #颜色透明度

                fig, ax = plt.subplots()     #调用图表方法
                index = np.arange(count)

                rects1 = plt.bar(index, num_tuple, bar_width, alpha=opacity, color='b', label='champion')    #这一块是核心
        
                #plt.xlabel('统计词')       #定义x轴标签
                plt.ylabel('频次')          #定义y轴标签
                plt.title('词频统计结果')    #定义图表标题
                plt.xticks(index + bar_width, name_tuple)      #标记x轴各点的名称
                plt.ylim(0, 500)   #限制y轴数值上限
                plt.legend()    #直接调用放这里就好了

                plt.tight_layout()  #这个一样的都是为了为了更好的绘图

                plt.savefig('words_frequency.png')   #以图片形式保存
                
                msg.reply_image('words_frequency.png')   #回复图片
        else:
                msg.reply("我是可爱的文本词频统计机器人，请把你的链接发给我吧")
        
        print(msg.sender.name,':',msg.text,'Msg Type:',msg.type)
embed()     #堵塞线程，让微信保持登录状态

'''
yag = yagmail.SMTP(sender,password,'smtp.qq.com') #使用QQ的SMTP服务服务器
yag.send(recipients,'19100304 baichampion',str0)
'''