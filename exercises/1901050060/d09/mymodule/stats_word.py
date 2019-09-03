import re
import collections

count = int()


def stast_text_en(text, count):
    ''' 统计英文单词词频出现的次数 '''
    if type(text) == str:
        text1 = text.replace(',', ' ').replace('.', ' ').replace('--', ' ').replace('!', ' ').replace('*',' ')  # 清除不必要的字符
        text2 = text1.split()
        print(text2)
        print(collections.Counter(text2).most_common(count))
    else:
        raise ValueError('此文本为非字符串')

def stast_text_cn(text, count):
    ''' 统计中文词频出现的次数 '''
    if type(text) == str:
        text1 = text.replace('。', '').replace('，', '').replace('-', '').replace('*', '').replace('!', '').replace('\n','').replace(' ','').replace('"','')  # 清除不必要的字符
        print(collections.Counter(text1).most_common(count))
    else:
        raise ValueError('此文本为非字符串')


def stast_text(text, count):
    ''' 统计中文和英文词频出现的次数 '''
    if type(text) == str:
        print(stast_text_en(text, count) + stast_text_cn(text, count))
    else:
        raise ValueError('此文本为非字符串')