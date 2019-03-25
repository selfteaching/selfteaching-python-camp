#创建一个名为stats_text_en的函数
#使用字典（dict）统计字符串样本text中各个英文单词出现的次数
import re
def stats_text_en(text):
    '''1、使用字典（dict)统计text中每个英文单词出现的次数.
    2、添加类型检查，如果不是字符串类型为异常'''
    if type(text) == str:
        result = re.sub("[^A-Za-z]", " ", text.strip())
        d = {}    
        for x in result.split( ):
            if not x in d:
                d[x] = 1
            else:
                d[x] = d[x]+1
        return d
    else:
        raise ValueError ("This is not an str type")

def stats_text_cn(str):
    '''1、统计每个中文汉字出现的次数
    2、添加类型检查，如果不是字符串类型为异常'''
    if type(str) == str:
        result = re.findall(u'[\u4e00-\u9fff]+', str)#\u是unincode编码，u4e00是十六进制表达值
        rep = ''.join(result)
        resoult = {}
        for i in rep:
            resoult[i] = rep.count(i)
        return resoult
    else:
        raise ValueError ("This is not an str type")
stats_text_cn(str = "")

#定义stats_word函数，分别调用stats_text_en,stats_text_cn,输出合并词频统计结果

def stats_text(text_bn):
    '''1、调用stats_text_en和stats_text_cn函数
    输出合并词频统计结果
    2、添加类型检查，如果不是字符串类型为异常'''
    if type(text_bn) == str:
        str1 = {}
        str1["en"] = stats_text_en(text_bn)
        str1["cn"] = stats_text_cn(text_bn)
        return str1
    else:
        raise ValueError ("This is not an str type")