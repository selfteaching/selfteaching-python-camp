#创建一个名为stats_text_en的函数
#使用字典（dict）统计字符串样本text中各个英文单词出现的次数
text ='''The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.我们只中每个英文单词出现的次数'''
import re
import collections
def stats_text_en(text,count):
    '''1、使用字典（dict)统计text中每个英文单词出现的次数.
    2、添加类型检查，如果不是字符串类型为异常'''
    if type(text) != str: #如果不是字符串类型就抛出异常
        raise ValueError ("This is not an str type")
    elif type(count) != int:
        raise ValueError ("This is not an int type")

    result = re.sub("[^A-Za-z]", " ", text.strip())
    return collections.Counter(result.split()).most_common(count)

def stats_text_cn(text,count):
    '''1、统计每个中文汉字出现的次数
    2、添加类型检查，如果不是字符串类型为异常'''
    if type(text) != str: #如果不是字符串类型就抛出异常
        raise ValueError ("This is not an str type")
    elif type(count) != int:
        raise ValueError ("This is not an str type")
    result = re.findall(u'[\u4e00-\u9fff]+', text)#\u是unincode编码，u4e00是十六进制表达值
    rep = ''.join(result)
    return collections.Counter(rep).most_common(count)   


#定义stats_word函数，分别调用stats_text_en,stats_text_cn,输出合并词频统计结果
def stats_text(text_bn,count):
    '''1、调用stats_text_en和stats_text_cn函数
    输出合并词频统计结果
    2、添加类型检查，如果不是字符串类型为异常'''
    if type(text_bn) != str: #如果不是字符串类型就抛出异常
        raise ValueError ("This is not an str type")
    elif type(count) != int:
        raise ValueError ("This is not an int type")
    str1 = {}
    str1["en"] = stats_text_en(text_bn,count)
    str1["cn"] = stats_text_cn(text_bn,count)
    return str1 

