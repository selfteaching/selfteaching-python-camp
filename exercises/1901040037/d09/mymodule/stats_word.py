def stats_text_cn(text):
    from collections import Counter
    cn_characters  = []
    for charater in text:
        if '\u4e00'<= charater <= '\u9fff':
            cn_characters.append(charater)
    cnt = Counter()
    for charater in cn_characters:
        cnt[charater] += 1
    print(cnt.most_common(100))
    
    # counter = {}
    # cn_characters_set = set(cn_characters)
    
    # for charater in cn_characters_set:
    #     counter[charater] = cn_characters.count(charater)
        
    # return sorted(counter.items(),key=lambda x:x[1],reverse=True)

 
def stats_text_en(text):
    from collections import Counter
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element) and element.isascii():
            words.append(element)
    cnt = Counter()
    for word in words:
        cnt[word] += 1
    print(cnt)
    
    # counter = {}
    # word_set = set(words)
    
    # for word in word_set:
    #     counter[word] = words.count(word)
        
    # return sorted(counter.items(),key=lambda x:x[1],reverse=True)


def stats_text(text):
    return stats_text_cn(text) + stats_text_en(text)


text1 = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
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


text2="""
我是 1972 年出生的。从交通工具来看，我经历过出门只能靠步行，大街上都是牛车马车，机动车顶多见过拖拉机，到有自行车，到见过摩托车，到坐小汽车，到自己开车，到开有自动辅助驾驶功能的电动车…… 从阅读来看，我经历过只有新华书店，到有网络上的文字，到可以在当当上在线买到纸质书，到有了国际信用卡后可以在 Amazon 上第一时间阅读新书的电子版、听它的有声版，到现在可以很方便地获取最新知识的互动版，并直接参与讨论…… 从技能上来看，我经历过认为不识字是文盲，到不懂英语是文盲，到不懂计算机是文盲，到现在，不懂数据分析的基本与文盲无异……
我也见识过很多当年很有用很赚钱很令人羡慕的技能 “突然” 变成几乎毫无价值的东西，最明显的例子是驾驶。也就是二十多年前，的哥还是很多人羡慕的职业呢！我本科的时候学的是会计专业，那时候我们还要专门练习打算盘呢！三十年之后的今天，就算有人打算盘打得再快，有什么具体用处嘛？我上中学的时候，有个人靠出版字帖赚了大钱 —— 那时候据说只要写字漂亮就能找到好工作；可今天，写字漂亮与否还是决定工作好坏的决定性因素吗？打印机很便宜啊！
"""

#防止以后把他当成模块调用的时候，这些模块不会执行。
#就是说，在别的地方引用的这个的时候，下面这个不会执行
if __name__ == '__main__':
    en_result = stats_text_en(text1)
    cn_result = stats_text_cn(text2)
    print(en_result)
    print(cn_result)
    
    # text = text1+text2
    # result = stats_text(text)
    # print(result)