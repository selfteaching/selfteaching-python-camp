# texten 和 textch 是测试文本
texten = '''
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
'''

textch = '''
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
def stats_text_en(text):
    '''This function aims to count English words. '''
    
    #去掉文本中除英文单词外的符号
    text1 = text.replace('\n',' ').replace('*',' ').replace('--','')
    text1 = text1.replace('!','').replace(',','').replace('.','')
    
    #将英文单词分出
    text1 = text1.split(' ')
    
    #去掉空值
    text1 = list(filter(None,text1))
    
    #统计每个英文单词出现的频率
    dic = {}
    for i in text1:
        dic.update({i:text1.count(i)})
    
    #按词频降序排列
    dic2 = sorted(dic.items(),key = lambda x:x[1],reverse = True)
    #print(dic2)
    return dic2
stats_text_en(texten)

#封装统计中文汉字字频的函数
def stats_text_cn(text):
    '''This function aims to count single Chinese words.'''
    
    con = set(text)  #筛选出文本中的唯一值
    con1 = list(con) #将集合转换成列表
    le = len(con1)  #计算con1的长度
    k = []
    dic = {}
    
    #筛选出文本中的汉字
    for i in range(le):
        if '\u4e00' <= con1[i] <= '\u9fff':
            k.append(con1[i])

    #统计每个汉字出现的频率        
    for m in k:
        dic.update({m:text.count(m)})

    #给统计结果按降序排列
    dic2 = sorted(dic.items(),key = lambda x:x[1],reverse = True)
    #print(dic2)
    return dic2

stats_text_cn(textch)