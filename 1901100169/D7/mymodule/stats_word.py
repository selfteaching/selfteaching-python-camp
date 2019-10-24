#封装统计英文单词词频的函数
text='''
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
def stats_text_en(text):
    elements = text.split() # 形成单词列表，通过string的split()将字符串切成数组
    words = [] #定义一个列表，列表用[]括起
    symbols = ',.-*!' # 标示出标点符号
    for element in elements: 
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element):
            words.append(element)
    #print('正常的英文单词',words)
    counter = {}
    word_set = set(words)
    for word in word_set:
        counter[word] = words.count(word)
    #print('英文单词出现的次数',counter)
    print('英文字数并按降序排列',sorted(counter.items(), key=lambda x:x[1],reverse=True))

print(stats_text_en(text))

import re
text1='''
蜀人杜渭江朝绅令麻城，居官执法，不敢干以私。
一日宴乡绅，梅西野倡令，要拆字入俗语二句。
梅云：“单奚也是奚，加点也是溪，除却溪边点，加鸟却为鸡。
俗语云：得志猫儿雄似虎，败翎鹦鹉不如鸡。”
毛石崖云：“单青也是青，加点也是清。
除却清边点，加心却为情。
俗语云：火烧纸马铺，落得做人情。”
杜答云：“单相也是相，加点也是湘。
除却湘边点，加雨却为霜。
俗语云：各人自扫门前雪，莫管他家瓦上霜。”
又云：“单其也是其，加点也是淇。
除却淇边点，加欠却为欺。
俗语云：龙居浅水遭虾戏，虎落平阳被犬欺。” 
（《古今谭概·谈资部·梅、郭二令相同》）
'''
def stats_text_cn(text1):
    p=re.compile(r'[\u4e00-\u9fa5]') # 中文的编码范围是\u4e00到\u9fa5]
    res=re.findall(p,text1) #Chinese choosen
    counter={}
    for i in res:
        counter[i]=res.count(i)
    counter=sorted(counter.items(),key=lambda x:x[1],reverse=True)
    print('中文字数统计',counter)
    return
print(stats_text_cn(text1))

#分别调用以上两个函数，输出合并词频统计结果
def stats_text(text_en_cn):
    return(stats_text_cn(text_en_cn)+stats_text_en(text_en_cn))