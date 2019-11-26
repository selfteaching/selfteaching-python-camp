import stats_word
import os

with open('D:\\文档\\Pythonlernen-ss01\\selfteaching-python-camp\\exercises\\1901050193\\d09\\mymodule\\tang300.json',mode='r', encoding='UTF-8') as f:
    text = f.read()
    #从文件读取指定的字节数，如果未给定或为负则读取所有。

try:
    print("唐诗三百首中的词频前 20 的词和词频数:\n",stats_word.stats_text_cn(text,20))
except ValueError:
    print('非字符串，请重新输入')