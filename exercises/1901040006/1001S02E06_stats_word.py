import re

#一、 封装统计英⽂单词词频的函数
#1. 创建⼀个名为 1001S02E06_stats_word.py 的⽂件
#2. 定义⼀个名为 stats_text_en 的函数，函数接受⼀个字符串 text 作为参数
#3. 实现该函数的功能（同 day5 任务 2）：统计参数中每个英⽂单词出现的次数，最后返回⼀个按词频降序排列的数组
#4. 为 stats_text_en 添加注释说明
#二、封装统计中⽂汉字字频的函数
#1. 在 1001S02E06_stats_word.py 中定义⼀个名为 stats_text_cn 的函数，函数接受⼀个字符串 text 作为参数
#2. 实现该函数的功能：统计参数中每个中⽂汉字出现的次数，最后返回⼀个按字频降序排列的数组
#3. 为 stats_text_cn 添加注释说明

text = '''
Beautiful is better than ugly.
Explicit is better than implicit.
没有自学能力的人没有未来！。
'''

def stats_text_en(text):
    '''统计字符串里每个英文单词的词频，返回按照词频降序排列的数组'''
    
    #提取字符串里的英文单词
    word_list = re.findall('[A-Za-z]+', text)
    #统计词频
    Word_dict = {word:word_list.count(word) for word in word_list}
    #排序
    result = sorted(Word_dict.items(),key = lambda items:items[1],reverse = True)
    print(result)
    return result

def stats_text_cn(text):
    '''统计字符串里每个汉字的词频，返回按照词频降序排列的数组'''
    
    #提取字符串里的英文单词
    word_list = re.findall('[\u4e00-\u9fa5]', text)
    #统计词频
    Word_dict = {word:word_list.count(word) for word in word_list}
    #排序
    result = sorted(Word_dict.items(),key = lambda items:items[1],reverse = True)
    print(result)
    return result

stats_text_en(text)
stats_text_cn(text)