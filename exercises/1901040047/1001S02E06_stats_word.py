# 利用的是day5的作业，把day5的作业封装进day6的函数中
t = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
人民网北京4月14日电 近期，图片版权交易问题备受社会各界关注。为推动媒体融合向纵深发展，更好整合媒体图片资源，保护创作者合法权益，人民网倡议主流媒体在净化版权市场一事上主动
担当。

人民网向全国党报、党刊、党台、党网发出四点倡议：

一、全国主流媒体应尽快在图片采编、使用和版权交易等方面形成联动机制，实现共融互通，建立合作联盟，成为图片市场的一支重要力量。人民网旗下的“人民图片网”愿与兄弟媒体携手探索。

二、探索新机制新模式，以“图片库集群”方式完成图片大数据采集、存储、共享，为主流媒体提供便捷高效的图片管理服务系统，搭建一个优质新闻图片版权交易平台。

三、加强图片版权认证及交易乱象舆论监督，积极引导图片版权交易市场的规范良性发展，让著作权人、版权所有人有尊严地创收增收。

四、高效配置社会公共资源，把拥有大量优质图片资源的机构平台有效组织起来，扩大主流价值影响力版图，助力整个图片版权交易市场的健康发展。

'''
# 给自己的英文排序函数写个说明
# 1.去标点符号，改小写，分割字符串
# 2.定义字典b{}
# 3.用.count（）把分割成字符串的单词和词频统计出来然后加入字典b
# 4.定义一个参数c，用sorte()函数对b进行排序
# 5.print缩进函数里面就是函数的一个输出参数了
import re # 调用正则表达式模块
          # re.sub(pattern, repl, string, count=0, flags=0)
def stats_text_en(t_en): # 定义函数
    a = t_en.replace(',','').replace('.','').replace(':','').replace(';','').replace('"','').replace('!','').replace('?','').replace('、','').replace('，','').replace('。','').replace('“','').replace('”','').replace('：','').replace('；','').replace('\n','').replace('！','').replace('？','').replace('/','').replace('*',' ').replace('--',' ')
    a = a.lower() # 全英文单词小写
    a = re.sub("[^A-Za-z]", " ", a) # 借用了这个正则表达式，这里保留了英文单词，^代表取出大小写a-z以外所有的字符串剔除
    a = a.split() # 分割字符串
    b = {}
    for i in a:
        count =  a.count(i)
        r1 = {i:count} 
        b.update(r1)
    c = sorted(b.items(),key=lambda x:x[1],reverse=True) 
    print('英文单词统计频率如下： \n',c) # 这里print()函数缩进就是封装进我定义的函数里面去了

# 给自己的中文排序函数写个说明
# 1.去标点符号
# 2.定义字典e{}
# 3.用.count（）把中文字符串的字和字频统计出来然后加入字典e
# 4.定义一个参数f，用sorted()函数对f进行排序
# 5.print缩进函数里面就是函数的一个输出参数了
def stats_text_cn(t_cn):
    d = t_cn.replace(',','').replace('-',' ').replace('.','').replace(':','').replace(';','').replace('"','').replace('!','').replace('?','').replace('、','').replace('，','').replace('。','').replace('“','').replace('”','').replace('：','').replace('；','').replace('\n','').replace('！','').replace('？','').replace('/','').replace('*',' ').replace(' ','')
    d = re.sub("[A-Za-z0-9]", "",d) #借用了这个正则表达式，这里删除了英文单词，因为没有加上^
    e = {}
    for j in d:
        count = d.count(j)
        r2 = {j:count}
        e.update(r2)
    f = sorted(e.items(),key=lambda x:x[1],reverse=True)
    print('中文单字统计频率如下： \n',f)

stats_text_en(t)
stats_text_cn(t)
