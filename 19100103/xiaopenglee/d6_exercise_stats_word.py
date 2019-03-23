text = '''
The Zen of Python, by Tim Peters
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
Namespaces are one honking great idea！
'''
#先将text里的标点符号去除
symbol = ",.!-*"
for str in symbol:
    text = text.replace(str,'')

#创建一个名为stats_text_en的函数
#使用字典（dict）统计字符串样本text中各个英文单词出现的次数
import re
def stats_text_en(text):
    '''使用字典（dict)统计text中每个英文单词出现的次数.'''
    result = re.sub("[^A-Za-z]", " ", text.strip())
    d = {}    
    for x in result.split( ):
        if not x in d:
            d[x] = 1
        else:
            d[x] = d[x]+1
    return d
print("统计text中每个英文单词出现的次数")
print(stats_text_en(text))
frequency = stats_text_en(text)
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
print("统计text中中文汉字出现的次数")
print(stats_text_cn(text))