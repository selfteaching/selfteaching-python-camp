#1.统计英文单词词频
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
'''

def stats_text_en(text): #统计英文单词出现的次数，按词频降序排列
    text=text.lower()   #把单词全部变为小写
    for p in ['~','!','@','#','$','%','^','&','*','(',')','_','+','|','{','{','[','.','-',',',';',':']:
        text=text.replace(p," ")  #去除标点符号
    text=text.split()   #把字符串分割成单个单词列表
    from collections import Counter
    res = Counter(text)
    d = dict(res)
    d = sorted(d.items(), key=lambda y: y[1], reverse=True) 
    return d

#测试
print(stats_text_en(text)) 



#2.统计中文汉字字频
text1='''
乡愁是一份沉重的爱。离开故土的游子，默默将爱收藏在心底。在异乡打拼，心里异常孤独，对着城市的钢筋水泥，对着那些永远都不可能与之说心里话的人，心中充满惆怅。在寂寞的时候，对着荷塘月色，想起故乡的袅袅炊烟，想起脸上堆满皱纹的阿爸阿妈，想起故乡的那条清澈的小河，想起儿时的玩伴，心中不由泛起甜蜜而酸涩的涟漪。
乡愁是一份深沉的爱。想起余光中的一首诗：小时候//乡愁是一枚小小的邮票//我在这头//母亲在那头//长大后//乡愁是一张窄窄的船票 我在这头//新娘在那头//后来啊//乡愁是一方矮矮的坟墓//我在外头//母亲啊在里头//而现在//乡愁是一湾浅浅的海峡//我在这头//大陆在那头。乡愁，承载着游子多少牵挂，多少痴缠的情感，多少浓烈的爱意，多少望穿秋水的期盼。
对母亲的牵挂，是乡愁中最浓烈的爱。想起母亲年轻时那乌黑的长发，发中飘散着游子熟悉的发香。小时候，游子时常依偎在母亲的怀中，听母亲讲河神的故事。对游子来说，母亲就是那条小河，有着清澈的眼睛，有着丰盈的乳汁，有着对自己细水长流爱。母爱如水，他如河旁的小草。从小到大，那条母亲河源源不断地滋润着他，陪伴他成长。
对父亲的牵挂，是乡愁中最深沉的爱。父亲，往往不苟言笑。在游子眼中，看得最多的往往是父亲伟岸的背影。父亲的背影，像山一样高大挺拔。小时候，常常趴在父亲的背上，感受父亲背上的温暖。父爱如山，他默默的守护着母亲，守护着游子，守护着这个暖意融融的家。父亲的背影，永远铭刻在游子的心里，无论岁月怎么侵蚀他的记忆，那熟悉的背影永远刻骨铭心。
对爷爷的牵挂，是乡愁中最和蔼可亲的爱。除了父母，爷爷便是占据游子记忆的亲人。爷爷满头白发，皱纹堆满了额头，总是抽着水烟，抽烟时发出“吧嗒”“吧嗒”的响声。爷爷经常在河边钓鱼，游子总是坐在爷爷身边，看爷爷聚精会神的等鱼上钩。最开心的，莫过于爷爷钓了一大篮子的鱼，这些小鱼便是游子最丰盛的晚餐。
对奶奶的牵挂，是乡愁中最温柔的爱。奶奶有一头整齐的而柔顺的白发，天庭饱满，温柔善良。奶奶善于织布，纳鞋。奶奶织的衣服是这个世界上最合身的衣服，奶奶纳的鞋是世上最结实的鞋。游子对奶奶有一种特殊的情感。奶奶最疼的人就是他。奶奶的笑容，如天上的太阳，总是那样灿烂。奶奶的笑，融化在游子心底，每当他不开心的时候，奶奶的笑便是他的创可贴。
对妻子的牵挂，是乡愁中最柔软的爱。妻子温柔似水，温婉贤惠。妻子的笑容，是这个世上最温暖美丽的笑容。妻子有一双会说话的大眼睛，皮肤白皙。她的笑容，像花一样绽放在游子心底。妻子的声音，甜美动人，游子最喜欢听她唱歌。妻子做得一手好菜，游子最喜欢吃她做的凉拌面条和麻婆豆腐。来到这个城市，每当孤独的时候，妻子的音容笑貌总是出现在他的脑海中。
对女儿的牵挂，是乡愁中最亲切的爱。女儿长得像红苹果，小脸红扑扑的，说话奶声奶气。每当游子回乡，第一个出来迎接的总是他可爱的女儿。女儿年纪虽小，但很贴心懂事。每当游子回乡，她会给游子准备好刮胡须的刀，端上一杯暖暖的水，用盆装好热水，帮游子洗脚，吃饭的时候，会夹最好吃的菜给游子。女儿的可爱乖巧，是远在他乡打工的游子最大的安慰。
'''

def stats_text_en(text1):    #统计中文汉字出现的次数，按词频降序排列
    for p in ['！','@','￥','%','……','&','*','（','）','—','+','{','}','：','“','《','》','？','，','。','、','；']:
        text1=text1.replace(p," ")  #去除标点符号
    d={}
    for s in text1:
        if '\u4e00' <= s <= '\u9fff':   # 中文字符范围
            d.setdefault(s,text1.count(s))
    d = sorted(d.items(), key=lambda y: y[1], reverse=True) 
    return d

#测试
print(stats_text_en(text1))
