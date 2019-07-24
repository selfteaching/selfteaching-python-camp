 # 统计text中每个英语单词出现的次数
 # 返回一个按词频降序排序的数组
def stats_text_en(text):
    words = []
    # 1): text to list
    elements = text.split()
    # 2): del symbol such as ,.*-! in every words
    for e in elements:
        for s in ',.*-!':
            e = e.replace(s,'')
        if(len(e)):
            words.append(e)
    # 3): count every words
    counter ={}
    wordset = set(words)
    for w in wordset:
        counter[w] = words.count(w)
    
    # 4): sort counter
    # 发现一个特点，这里对counter排序后，其实并不会改变counter，
    # 也就是排序后的结果需要另一个对象保存。这和C语言有很明显的不同。
    return sorted(counter.items(),key=lambda x: x[1],reverse=True)

 # 统计text中每个汉字出现的次数。返回一个字频降序排序的数组
 # 思考：
 # 1、对比，文单词以空格为分割，可用split函数分割出。而中文呢？中文汉字是固定长度。
 #    不用考虑分割问题。计数汉字，就和计数英语字符一样。
 # 2、中英文混合情况需要考虑吗？这又涉及到单词or汉字的判断。先从简单开始，仅考虑只有汉字情况。
def stats_text_cn(text):
    counter = {}
    wordset = set(text)
    for w in wordset:
        counter[w] = text.count(w)
    return sorted(counter.items(),key=lambda x: x[1],reverse=True)

text = ''' The Zen of Python, by Tim Peters
Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambxiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!
'''
print(stats_text_en(text))

text2 = '''学习学习再学习 666'''
print(stats_text_cn(text2))

'''
#Day 6 练习感受
例子非常好，统计英语单词词频，再到统计汉字字频。感觉很实用，容易触发思考。
急需更多这样使用的小函数，小功能，小项目的训练。
'''