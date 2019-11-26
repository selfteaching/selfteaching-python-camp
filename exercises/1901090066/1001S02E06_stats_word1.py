text='''
The Zen of Python, by Tim Peters.


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
    # 将text全部变成小写，将符号变为空格，将字符串分割
    text=text.lower()
    txt= text.replace('\n', ' ').replace('.', ' ').replace('!', ' ').replace('--', ' ').replace('.',' ').replace('*',' ')
    txt1=txt.split()
    counts = {}
    # 如果字典里再次出现该单词，次数加一，否则次数为一
    for text in txt1:
        if text in counts.keys():
            counts[text] = counts[text] + 1
        else:
            counts[text] = 1
    #排序，从高到低
    count_text=sorted(counts.items(),key=lambda x:x[1],reverse=True)
    return count_text
print (stats_text_en(text))


