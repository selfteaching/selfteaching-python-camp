import pprint
import re

text = '''1. 在 1001S02E06_stats_word.py 中定义⼀一个名为 stats_text_cn 的函数，函数接受⼀一 个字符串串 text 作为参数
2. 实现该函数的功能:统计参数中每个中⽂文汉字出现的次数，最后返回⼀一个按字频降序排列列的 数组
3. 为 stats_text_cn 添加注释说明he Zen of Python, by Tim Peters Beautiful is better than ugly.
Explicit is better'''

#字符串文本按照单词排序
def stats_text_en(text):
    pattern = re.compile( "[A-Z]*[a-z]+")
    word_list = re.findall(pattern,text)
    dic = {}
    for item in word_list:
        if item not in dic:
            dic[item] = 1
        else:
            dic[item] += 1
    dic = sorted(dic.items(),key = lambda x:x[1],reverse = True)

    return dic


#参数：字符串文本，输出按汉子的统计排名
def stats_text_cn(text):
    pattern1 = re.compile( "[\u4E00-\u9FA5]")
    new_list = re.findall(pattern1,text)
    dic1 = {}
    for item in new_list:
        item = item.strip()
        if item not in dic1:
            dic1[item] = 1
        else:
            dic1[item] += 1        
    #把汉子装入词典
    dic1 = sorted(dic1.items(),key = lambda x:x[1] ,reverse = True)

    return dic1

pprint.pprint(stats_text_en(text))