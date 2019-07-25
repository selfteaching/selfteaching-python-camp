#创建一个函数，接收字符串text作为参数
def stats_word_en(text):
    """
    stats_word_en 可接收一个英文字符串text作为参数，统计参数中每个英文单词出现的次数，最后返回一个按词频降序排列的数组
    """
    #创建一个空列表
    words = []
    #想要删除的标点符号
    symbols = '.,!-*'
    #将字符串text分割后赋值给elements，其中包含标点符号，英文单词，和空格，elements数据格式为列表
    elements = text.split()
    #遍历elements中的每一个element
    for element in elements:
    #遍历标点符号
        for symbol in symbols:
            #将标点符号替换为空格，并赋值给element，element是字符串
            element = element.replace(symbol,'')
            #如果element不是空字符，即element是单词，将单词添加到words列表中
        if len(element) > 0:
            words.append(element.lower())
    #print(words)
    #创建word_set集合，将重复单词去重
    word_set = set(words)
    #print(word_set)
    #创建字典
    counter = {}
    for word in word_set:
        counter[word] = words.count(word)
    return sorted(counter.items(),key = lambda x:x[1],reverse = True)
    #将字典按照单词词频为参数进行降序排列
    #print(sorted(counter.items(),key = lambda x:x[1],reverse = True))


#定义一个函数,以text作为参数
def stats_word_cn(text):
    """
    stats_text_cn接收一个中文字符串text作为参数，统计参数中每个汉字出现的次数，最后返回一个按字频降序排列排列的数组
    """
    #建立一个列表
    cn_characters = []
    #遍历列表text
    for character in text:
    #如果是汉字，则加入列表中,\u4e00----\u9fff 是Unicode中中文字符的范围
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    #建立一个字典
    cn_counter = {}
    #建立集合将文本去重
    character_set = set(cn_characters)
    for character in character_set:
        cn_counter[character] = cn_characters.count(character)
    #返回按字频降序排列的数组
    return sorted(cn_counter.items(),key = lambda x:x[1],reverse= True)
    #print(sorted(cn_counter.items(),key = lambda x:x[1],reverse = True))

sample_text_1 = '''
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
sample_text_2 = '''
编程作为 “讲解如何习得自学能力的例子”，实在是太好了。

首先，编程这个东西反正要自学 —— 不信你问问计算机专业的人，他们会如实告诉你的，学校里确实也教，但说实话都教得不太好……

其次，编程这个东西最适合 “仅靠阅读自学” —— 这个领域发展很快，到最后，新东西出来的时候，没有老师存在，任由你是谁，都只能去阅读 “官方文档”，只此一条路。

然后，也是最重要的一条，别管是不是很多人觉得编程是很难的东西，事实上它就是每个人都应该具备的技能。

许多年前，不识字，被称为文盲……

后来，人们反应过来了，不识英文，也是文盲，因为科学文献的主导语言是英文，读不懂英文，什么都吃不上热乎的；等菜好不容易端上来了吧，早就凉了不说，味道都常常会变……

再后来，不懂基本计算机操作技能的，也算是文盲，因为他们无论做什么事情，效率都太低下了，明明可以用快捷键一下子完成的事情，却非要手动大量重复……

到了最近，不懂数据分析的，也开始算作文盲了。许多年前人们惊呼信息时代来了的时候，其实暂时体会不到什么太多的不同。然而，许多年过去，互联网上的格式化数据越来越多，不仅如此，实时产出的格式化数据也越来越多，于是，数据分析不仅成了必备的能力，而且早就开始直接影响一个人的薪资水平。

你作为一个个体，每天都在产生各种各样的数据，然后时时刻刻都在被别人使用着、分析着…… 然而你自己却全然没有数据分析能力，甚至不知道这事很重要，是不是感觉很可怕？你看看周边那么多人，有多大的比例想过这事？反正那些天天看机器算法生成的信息流的人好像就是全然不在意自己正在被支配……

怎么办？学呗，学点编程罢 —— 巧了，这还真是个正常人都能学会的技能。
'''
print(stats_word_en.__doc__)
print(stats_word_en(sample_text_1))
help(stats_word_cn)
print(stats_word_cn(sample_text_2))