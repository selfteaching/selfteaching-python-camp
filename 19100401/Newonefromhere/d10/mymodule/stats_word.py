# text 是测试文本
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
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

余周周是一个出生在八十年代末的普通小姑娘，
和妈妈相依为命，在漫长孤寂的童年中，最好的朋友叫奔奔。
进入小学后她在林杨和陈桉的帮助下，度过了初期学习拼音的艰难和对学校的不适，
逐渐在学校里面成了小有名气的文艺骨干。

在初中余周周逐渐放开手脚如鱼得水，
并且和儿时最亲密的小伙伴奔奔重逢。
余周周和班级里面成绩最差也最古怪木讷的女生辛美香成了朋友，
经过努力，辛美香和余周周一同考入了省重点振华高中。

升入振华高中的余周周经历了许多波折。
与林杨的重逢，对陈桉的深入了解，情窦初开的暗恋，
重点高中内部因为成绩排名出国机会和保送名额等等而引发的“金枝欲孽”。
外婆的病重让妈妈和几个舅妈之间矛盾重重……诸多事情让余周周急速成长。

你好,旧时光
你好,旧时光
高中毕业，曲终人散，青春不朽。
每一个细微的地方都能勾起大家的无尽回忆，回忆当初的那些人 jj 那些事。
《你好，旧时光》（又名：玛丽苏病例报告）是青春文学作家八月长安所作的青春小说。
主要讲述了余周周童年、青少年时期的故事。
'''

#1 封装统计英文单词词频的函数
def stats_text_en(text,count):
    '''This function aims to count English words. '''
    
    #导入 collections 模块中的 Conuter,统计词频
    from collections import Counter

    #检查参数类型是否为字符串
    if isinstance(text,str):
        pass
    else:
        raise ValueError #不是字符串报错
        

    #筛选出文本中的英文部分
    result = ''.join(j for j in text if ord(j)<256)
    
    #去掉文本中除英文单词外的符号
    text1 = result.replace('\n',' ').replace('*',' ').replace('--','')
    text1 = text1.replace('!','').replace(',','').replace('.','')
    
    #将英文单词分出
    text1 = text1.split(' ')
    
    #去掉空值
    text1 = list(filter(None,text1))

    
    #统计每个英文单词出现的频率
    sort_en = Counter(text1).most_common(count)
    
    #print(sort_en)
    return sort_en
stats_text_en(text,10)

#封装统计中文汉字字频的函数
def stats_text_cn(text,count):
    '''This function aims to count single Chinese words.'''

    #检查参数类型是否为字符串
    if isinstance(text,str):
        pass
    else:
        raise ValueError #不是字符串报错
    
    from collections import Counter
    import jieba     #导入分词库
    
    #统计任意汉字词频
    words = jieba.cut(text) #分词
    k = []
    for i in words:
        if len(i) > 1 and '\u4e00' <= i <= '\u9fff': #剔除英文和其他符号
            k.append(i)
    
    sort_cn = dict(Counter(k).most_common(count)) #统计词频
    #print(sort_cn)
    return sort_cn

stats_text_cn(text,10)

#创建 stats_text 函数，分别调用 stats_text_en,stats_text_cn
def stats_text(text,count):
    '''This function aims to count Chinese and English

    words.'''
 
    #检查参数类型是否为字符串
    if isinstance(text,str):
        pass
    else:
        raise ValueError #不是字符串报错

    return stats_text_en(text,count),stats_text_cn(text,count)

#输出 tang300.json 文件中词频前 20 的词和词频数
import os
os.chdir(r'D:\用户目录\我的文档\GitHub\selfteaching-python-camp\19100401\Newonefromhere\d10')
f = open('tang300.json','r',encoding='utf8')
text2 = f.read()
resl_cn = stats_text_cn(text2,20)
f.close()
print(resl_cn)