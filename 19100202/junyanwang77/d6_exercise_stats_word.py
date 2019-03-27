text = '''
The Zen of Python, by Tim Peters

美丽 is better than 丑陋.
清楚 is better than 含糊.
简单 is better than 复杂.
复杂 is better than 难懂.
单一 is better than 嵌套.
稀疏 is better than 稠密.
Readability counts.
Special cases aren't special enough to 打破规则.
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
#去除text里的标点符号
symbol = ",.!-*"
for str in symbol:
        text = text.replace(str,'') 
print(text)
#创建一个名为stats_text_en的函数
#使用字典（dict）统计字符串样本text中各个英文单词出现的次数
import re
def stats_text_en(text):  #定义函数 stats_text_en()，接收参数text
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

print(stats_text_en(text))
frequency = stats_text_en(text)
print("按照出现次数从大到小输出所有的单词及出现的次数")
print (sorted(frequency.items(), key=lambda frequency: frequency[1],reverse=True))


#创建一个名为stats_text_cn的函数，功能：统计每个中文汉字出现的次数
import re
def stats_text_cn(text):
    '''统计每个中文汉字出现的次数'''
    result = re.findall(u'[\u4e00-\u9fff]+', text)#\u是unincode编码，u4e00是十六进制表达值
    rep = ''.join(result)
    resoult = {}
    for i in rep:
        resoult[i] = rep.count(i)
    return resoult
stats_text_cn(text = "")
print(stats_text_cn(text))
frequency = stats_text_cn(text)
print("按照字频降序排列")
print (sorted(frequency.items(), key=lambda frequency: frequency[1],reverse=True))