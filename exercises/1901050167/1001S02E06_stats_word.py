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
def stats_text_en(text):
    for ch in  '!,.--':
        text=text.replace(ch,"")#将文本中特殊字符替换成空格
    return text
text1=stats_text_en(text)
textlist1 = text1.split()    #切分字符
textlist2=[]                  #建立数组
for i in textlist1:         #遍历列表中的元素
    if i.isalpha():         #检查字符串中是否只包含字母
        textlist2.append(i) #如果是，在列表的尾部把i加上               
counts = {}                  #生成一个空字典
for word in textlist2:               #遍历列表list2
    counts[word]=counts.get(word,0)+1#给字典中出现的词计数
items=list(counts.items())        #将单词与对应的计数的键对值列表
items.sort(key=lambda x:x[1],reverse=True)#排序
print("{}".format(items))

txt='''不同的人会呈现不同的应对生活的状态，是因为他们本身属于两种不同思维模式的人，
所以受到自身思维模式的影响，产生了两种截然不同的生活。
固定性思维模式和成长型思维模式。
固定性思维模式的人往往相信自己的才能是一成不变的，
以至于在面对困境等等时候采取的往往是消极的态度，并时常进行自我怀疑，很难做出突破性的改变。
成长型思维模式的人往往会认为自己的能力是可以发展的，
所以在面对困境与压力的时候，总会找到合适的进步空间，让自己突破自己，积极地应对生活。'''
def stats_text_cn(txt):
    for ch in  '!，。--':
        txt=txt.replace(ch,"")#将文本中特殊字符替换成空格
    return txt
    for ch in txt:
        if '\u4e00' <= ch <= '\u9fff':
            return txt
    return False
txt1=stats_text_cn(txt)            
counts2 = {}                  #生成一个空字典
for words in txt1:               #遍历txt1
    counts2[words]=counts2.get(words,0)+1#给字典中出现的词计数
items2=list(counts2.items())        #将单词与对应的计数的键对值列表
items2.sort(key=lambda x:x[1],reverse=True)#排序
print("{}".format(items2))



