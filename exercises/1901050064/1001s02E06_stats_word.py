#1001s02E06_stats_word.py
#1.封装统计英文单词词频的函数
text = '''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sqarse is better than dense.
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
def stats_text_en(text):  #定义函数，接受一个字符串作为参数
    elements = text.split()
    words = []
    symbols = ',.*-!'     #对样本文本挑选出需要剔除的非单词符号
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')    #逐个替换字符号，用''是为了同时剔除符号所占的位置
        if len(element):
           words.append(element)
    print('正常的英文单词==.',words)
    counter = {}
    word_set = set(words)
    for word in word_set:
        counter[word] = words.count(word)
    print('英文单词出现的次数 ==>',counter)
#按照出现次数从大到小输出所有的单词及出现的次数
    print('从大到小输出所有的单词及出现的次数==>',sorted(counter.items(),key=lambda x:x[1],reverse=True ))
stats_text_en(text)

#2.封装统计中文汉字字频的函数
text = '''
美丽胜过丑陋。
显式优于隐式。
简单比复杂更好。
复杂比复杂更好。
优于嵌套。
稀疏优于密集。
可读性很重要。
特殊情况不足以打破规则。
虽然实用性胜过纯洁。
错误不应该默默地传递。
除非明确沉默。
面对困惑，拒绝猜测的诱惑。
应该有一个 - 最好只有一个 - 明显的方法来做到这一点。
虽然这种方式起初可能并不明显，除非你是荷兰人。
现在比永远好。
虽然现在永远不会比*正确好。
如果实施很难解释，这是一个坏主意。
如果实现很容易解释，那可能是个好主意。
命名空间是一个很棒的主意 - 让我们做更多的事情吧！
'''
import re    #调用正则表达式模块，从高手那里学来的
def stats_text_cn(text):
    d = text.replace(',','').replace('-',' ').replace('.','').replace(':','').replace(';','').replace('"','').replace('!','').replace('?','').replace('、','').replace('，','').replace('。','').replace('“','').replace('”','').replace('：','').replace('；','').replace('\n','').replace('！','').replace('？','').replace('/','').replace('*',' ').replace(' ','')
    d = re.sub("[A-Za-z0-9]", "",d) #借用了这个正则表达式，这里删除了英文单词，因为没有加上^
    e = {}
    for j in d:
        count = d.count(j)
        r2 = {j:count}
        e.update(r2)
    f = sorted(e.items(),key=lambda x:x[1],reverse=True)
    print('中文单字统计频率如下： \n',f)
stats_text_cn(text)

