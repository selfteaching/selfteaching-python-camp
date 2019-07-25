from mymodule import stats_word
from collections import Counter

#指定编码格式为utf-8打开文件
f=open(r"C:\Users\12931\Desktop\2019\python训练营\day01\selfteaching-python-camp\exercises\1901020071\day09\tang300.json",encoding='UTF-8')
#读物文件内容
text=f.read()
#关掉文件流
f.close()
#print(text)


#把文件里的汉字进行词频统计，并返回
countList=stats_word.stats_text_cn(text,100)
print(countList)


