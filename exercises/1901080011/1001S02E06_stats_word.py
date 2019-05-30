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

def stats_text_en(text):
    """统计英文单词词频"""
    text = text.replace("\n",' ')
    text = text.replace('.',' ')
    text = text.replace(',',' ')
    text = text.replace('--',' ')
    text = text.replace('*',' ')
    text = text.replace('!',' ')    
    words = text.split(' ')
    #过滤空字符串''
    while '' in words:
        words.remove('')
    #创建一个字典存储满足条件的值
    newWords = {}
    for word in words:
        if word in newWords.keys():
            newWords[word] += 1
        else:
            newWords[word] = 1
    newWords=sorted(newWords.items(),key=lambda x:x[1],reverse=True)
    return newWords

#print(stats_text_en(text))

text = '魏和河河河'
def stats_text_cn(text):
    """统计中文单词词频"""
    text = text.replace("\n",'')
    text = text.replace('.','')
    text = text.replace(',','')
    text = text.replace('--','')
    text = text.replace('*','')
    text = text.replace('!','')   
    #创建一个字典存储满足条件的值
    newWords = {}
    for word in text:
        if word in newWords.keys():
            newWords[word] += 1
        else:
            newWords[word] = 1
    newWords=sorted(newWords.items(),key=lambda x:x[1],reverse=True)
    return newWords

#print(stats_text_cn(text))