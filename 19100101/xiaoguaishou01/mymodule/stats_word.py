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
这是中文，为了测试代码效果
'''
#先将text里的标点符号去除
symbol = ",.!-*"
for str in symbol:
    text = text.replace(str,'')
#print(text)
#创建一个名为stats_text_en的函数
#使用字典（dict）统计字符串样本text中各个英文单词出现的次数
import re
def stats_text_en(text):
    '''统计次数.
    
    使用字典（dict)统计text中每个英文单词出现的次数.'''
    result = re.sub("[^A-Za-z]", " ", text.strip())
    d = {}    
    for x in result.split( ):
        if not x in d:
            d[x] = 1
        else:
            d[x] = d[x]+1
    return d


import re
def stats_text_cn(str):
    '''统计每个中文汉字出现的次数'''
    result = re.findall(u'[\u4e00-\u9fff]+', str)#\u是unincode编码，u4e00是十六进制表达值
    rep = ''.join(result)
    resoult = {}
    for i in rep:
        resoult[i] = rep.count(i)
    return resoult
stats_text_cn(str = "")

#定义stats_word函数，分别调用stats_text_en,stats_text_cn,输出合并词频统计结果

def stats_text(text_bn):
    '''调用stats_text_en和stats_text_cn函数
    
    输出合并词频统计结果'''
    str1 = {}
    str1["en"] = stats_text_en(text_bn)
    str1["cn"] = stats_text_cn(text_bn)
    return str1
    
    