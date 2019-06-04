text1 = '''
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
text2 = '''
感谢“蔡滢教练“提供真诚建议！
蔡滢教练拥有罕见匹敌的代码能力，同时，蔡滢教练杰出的 coding 方法也给学员带来了可见进步！
再次感谢，感谢！
'''



# 一、封装统计英文单词词频的函数
# 1、……
# 2、定义一个名为 stats_text_en 的函数，函数接受一个字符串 text 作为参数
# 3、实现该函数的功能（同 day5 任务2）：统计参数中每个英文单词出现的次数，最后返回一个按词频降序排列的数组
# 4、为 stats_text_en 添加注释说明
def stats_text_en(string):
   """
      1/ Counts the number of occurrences of each word in the parameter;
      2/ Returns an array in descending order of word frequency.
   """
   symbol_deleting_en = [',','.','!','-','*']
   for x in symbol_deleting_en:
      string = string.replace(x,'')
   string = string.lower()
   string = string.split()
   stats = dict([(word,string.count(word)) for word in string])
   stats = sorted(stats.items(),key=lambda item:item[1],reverse=1)
   return stats

result = stats_text_en(text1)
print (result,end="\n\n\n\n")



# 二、封装统计中文汉字字频的函数
# 1、在 d6_exercise_stats_word.py 中定义一个名为 stats_text_cn 的函数，函数接受一个字符串 text 作为参数
# 2、实现该函数的功能：统计参数中每个中文汉字出现的次数，最后返回一个按字频降序排列的数组
# 3、为 stats_text_cn 添加注释说明
def stats_text_cn(string):
   """
      1/ Counts the number of occurrences of each character in the parameter;
      2/ Returns an array in descending order of character frequency.
   """
   symbol_deleting_cn = ['~','！',"……",'，','。','：',"——","”","“"," ","\n"]
   for x in symbol_deleting_cn:
      string = string.replace(x,'')
   string = [character for character in string]
   stats = dict([(character,string.count(character)) for character in string])
   stats = sorted(stats.items(),key=lambda item:item[1],reverse=1)
   return stats

result = stats_text_cn(text2)
print(result)