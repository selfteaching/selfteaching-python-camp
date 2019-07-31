import collections
import re

#将中文进行词频统计。
def stats_text_cn(text):
    if type(text) == str:
        list1 = re.findall(r'[\u4e00-\u9fa5]', text)
        count = int(input("Please input the number of elements to be output in cn_text:"))
        word_frequencycount_cn = collections.Counter(list1).most_common(count)
        return print(word_frequencycount_cn)
    else:
        raise ValueError("The input is a non-string, please enter a string.")

#将英文进行词频统计。
def stats_text_en(text):
    if type(text) == str:
        #去除字符串中的中文字符
        for chara in text:
            if '\u4e00' <= chara <= '\u9fa5':
                text = text.replace(chara,",")
        #清洗英文字符串中的特殊字符
        for chara in ",.!-*？，。：「」、”\":{}\n！\\n］［；）□（““□（178][0123456789《》":
            text = text.replace(chara," ")
        #将字符串中的英文全部变成小写
        text = text.lower()
        list1 = text.split()
        #统计每个单词出现的词频
        count = int(input("Please input the number of elements to be output in en_text:"))
        word_frequencycount_en = collections.Counter(list1).most_common(count)
        return print(word_frequencycount_en)
    else:
        raise ValueError("The input is a non-string, please enter a string.")

#分别调用stats_text_en()函数和stats_text_cn()函数。
def stats_text(text):
    if type(text) == str:
        stats_text_cn(text)
        stats_text_en(text)
    else:
        raise ValueError("The input is a non-string, please enter a string.")