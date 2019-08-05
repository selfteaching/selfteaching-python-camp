text = '''
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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
# -*-coding:utf-8 -*-
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
#-------------------------解决大部分中文乱码的问题------------------------------------------

#封装统计英文单词词频的函数
def stats_text_en(text):#处理英文文本，按单词出现次数，降序排列
    text=text.replace('.',' ').replace(',',' ').replace('!',' ').replace('--',' ').replace('*',' ')#把非英文字符替换为空格
    text=text.lower()#把所有单词变为小写
    text=text.split()#以空格拆分为独立单词
    dic={}
    for i in text:  #将字符串转换为字典
        count=text.count(i)
        r1={i:count}
        dic.update(r1)
        #print(i,'',count )
    #print(dic)
    #print(end='\n')
    print("按出现次数从大到小排列")
    dic1=sorted(dic.items(),key=lambda x:x[1],reverse=True) #按照单词出现次数，从大到小排序
    print(dic1)

stats_text_en(text)

#封装统计中文汉字字频的函数
text = '''
我把那些能给你带来新视野，能让你改变思考模式，甚至能让你拥有一项新技能的内容称之为 “有繁殖能力的内容”。
人都一样，拥有什么样的能力之后，就会忍不住去用，甚至总是连下意识中也要用。
那些靠阅读机器算法推送的内容而杀时间的人，恰恰就是因为他们有阅读能力才去不断地读，读啊读，像是那只被打了兴奋剂后来死在滚轮上的小白鼠。如果这些人哪怕有一点点自学能力，那么他们很快就会分辨出自己正在阅读的东西不会刺激自己的产出，只会消磨自己的时间；那么，他们就会主动放弃阅读那些杀时间的内容，把那时间和精力自然而然地用在筛选有繁殖能力的内容，让自己进步，让自己习得更多技能上去了。
所以，只要你有一次 “只靠阅读习得一项新技能” 的经验，你就变成另外一个人了。你会不由自主、哪怕下意识里都会去运用你新习得的能力…… 从这个角度看，自学很上瘾！能上瘾，却不仅无害，还好处无穷，这样的好事，恐怕也就这一个了罢。
'''
                  
def stats_text_cn(text):    #定义检索中文函数
    cndic={} #初始化一个空的字典
    for i in text:
        if u'\u4e00' <= i <= u'\u9fff':#判断是不是中文
            count=text.count(i)
            r1={i:count}
            cndic.update(r1)
            #cndic[i] = text.count(i)
    #return cndic
    cndic=sorted(cndic.items(),key=lambda item:item[1],reverse = True) 
    print(cndic)
stats_text_cn(text)