text = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
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


# 二、统计字符串样本中英文单词出现的次数
# 1、创建一个名为 d5_exercise_stats_text.py 的文件
# 2、使用字典（dict）统计字符串样本 text 中各个英文单词出现的次数。
symbol_deleting = [',','.','!','-','*']                  # 将非词类字符均替换为空格
for x in symbol_deleting:
   text = text.replace(x,'')
text = text.lower()                                      # 将所有单词改为小写
text = text.split()                                      # 以空格为分隔符，分隔字符串text，使之成为列表text
stats = dict([(word,text.count(word)) for word in text]) # 使用list comprehension和dict()生成词典

# 3、按照出现次数从大到小输出所有的单词及出现的次数
stats = sorted(stats.items(),key=lambda item:item[1],reverse=1)
print(stats)