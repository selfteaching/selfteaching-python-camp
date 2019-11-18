
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
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''


def stats_text_en(text):#封装统计英⽂文单词词频的函数

    text=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')
    text=text.split()
    dict_test={}
    for i in text:  
        count=text.count(i)
        r1={i:count}
        dict_test.update(r1)

    return sorted(dict_test.items(),key=lambda x:x[1],reverse=True)
 

dict_test1 = stats_text_en(text)
print(dict_test1) 

cn_text='''1. 在 1001S02E06_stats_word.py 中定义⼀一个名为 stats_text_cn 的函数，函数接受⼀一
个字符串串 text 作为参数
2. 实现该函数的功能：统计参数中每个中⽂文汉字出现的次数，最后返回⼀一个按字频降序排列列的
数组
3. 为 stats_text_cn 添加注释说明'''

def stats_text_cn(text):
    cn_words = []
    for word in text:        
        if '\u4e00' <= word <= '\u9fff':
            cn_words.append(word)
    counter = {}
    cn_word_set = set(cn_words)
    for word in cn_word_set:
        counter[word] = cn_words.count(word)
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)

cn_result = stats_text_cn(cn_text)
print(cn_result) 


def stats_text(text):#实现功能：分别调⽤用stats_text_en , stats_text_cn ，输出合并词频统计结果
    link_word_1 = stats_text_en(text)
    link_word_2 = stats_text_cn(text)
    link_word = link_word_1 + link_word_2
    return link_word
 

