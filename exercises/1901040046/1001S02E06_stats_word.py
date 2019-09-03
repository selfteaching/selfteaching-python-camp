#将字符串s按照None的分隔切分为一个字符串组，并清洗字符串元素的标点符号，并统计不同字符是数量，最后以数量降序排列。
def stats_text_en(text):
    replace_text = text.replace(',','').replace('.','').replace('*','').replace('?','').replace('!','').replace('-','')
    split_text = replace_text.split()
    wordcount = {}
    for i in split_text:
        if i not in wordcount:
            wordcount[i] = 1
        else:
            wordcount[i] += 1
    wordcount = sorted(wordcount.items(),key=lambda x:x[1],reverse=True) 
    return wordcount

#定义一个用来统计汉字的函数.新增list函数将中文字符串切分。暂时不引人正则函数从而用来区分中英文。
def stats_text_cn(text):
    replace_text = text.replace('，','').replace('。','').replace('*','').replace('？','').replace('！','').replace('——','')
    list_text = list(replace_text)
    wordcount = {}
    for i in list_text:
        if i not in wordcount:
            wordcount[i] = 1
        else:
            wordcount[i] += 1
    wordcount = sorted(wordcount.items(),key=lambda x:x[1],reverse=True) 
    return wordcount


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
美丽 is better than 丑陋.
清楚 is better than 含糊.
简单 is better than 复杂.
复杂 is better than 难懂.
单一 is better than 嵌套.
稀疏 is better than 稠密.
可读性计数.
Special cases aren't special enough to 打破规则.
即使练习会使得不再纯粹.
但错误不应该用沉默来掩盖.
Unless explicitly silenced.
面对起义，拒绝猜的诱惑.
有且只有一个办法.
Although that way may not be obvious at first unless you're Dutch.
尝试总比从未试过要强.
Although never is often better than *right* now.
如果执行很难被解释，那将是一个很糟的想法.
如果执行很容易解释，这会是一个好点子.
'''

print(stats_text_en(text))
print(stats_text_cn(text))


