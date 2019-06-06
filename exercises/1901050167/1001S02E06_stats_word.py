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
def stats_text_en():
    for ch in '!,.--':
        text=text.replace(ch,"")
    textlist1 = text.split()
    textlist2 = []
    for i in textlist1:
        if i.isalpha():
            textlist2.append(i)
    dict1 = {}
    dict1 = dict1.fromkeys(textlist2)
    word_1 = list(dict1.keys())
    for i in word_1:
        dict1[i] = textlist2.count(i)
    dict2 = {}
    dict2 = sorted(dict1.items(),key=lambda d:d[1],reverse=True)
    dict2 = dict(dict2)
    return dict2
text1=stats_text_en(text)
print(text1)


txt='''不同的人会呈现不同的应对生活的状态，
是因为他们本身属于两种不同思维模式的人，所以受到自身思维模式的影响，
产生了两种截然不同的生活。
固定性思维模式和成长型思维模式。
固定性思维模式的人往往相信自己的才能是一成不变的，
以至于在面对困境等等时候采取的往往是消极的态度，并时常进行自我怀疑，
很难做出突破性的改变。
成长型思维模式的人往往会认为自己的能力是可以发展的，所以在面对困境与压力的时候，
总会找到合适的进步空间，让自己突破自己，积极地应对生活。'''
def stats_text_cn():
    txt1=[]
    for m in txt:
        if '\u4e00'<=m<='\u9fff':
            txt1.append(m)
    counts={}
    txt2=set(txt1)
    for n in txt2:
        counts[n]=txt1.count(n)
    return sorted(counts.items(),key=lambda x:x[1],reverse=True)
txt3=stats_text_cn(txt)
print(txt3)

    