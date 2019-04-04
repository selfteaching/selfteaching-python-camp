# 一、将统计中文字频和英文词频的函数封装为一个模块
# 1、添加一个名为 stats_text 的函数，实现功能：分别调用 stats_text_en, stats_text_cn，输出合并词频统计结果

from collections import Counter                                                  # /// day9 ///

# 1.1 封装统计英文单词词频的函数
def stats_text_en(string,count):                                                 # /// day9 /// 添加int类型变量 count，用于限制输出元素的个数
   """
      0/ check parameter type
      1/ Counts the number of occurrences of each word in the parameter;
      2/ Returns an array in descending order of word frequency.
   """
   if type(string) == str:
      symbol_deleting_en = [',','.','!','-','*']
      for x in symbol_deleting_en:
         string = string.replace(x,'')
      string = string.lower()
      string = string.split()
      stats = dict([(word,string.count(word)) for word in string])
      c = Counter(stats)                                                         # /// day9 ///
      stats = c.most_common(count)                                               # /// day9 ///
   #  stats = sorted(stats.items(),key=lambda item:item[1],reverse=1)
      return stats
   else:
      raise ValueError(string)

# 1.2 封装统计中文汉字字频的函数
def stats_text_cn(string,count):                                                 # /// day9 /// 添加int类型变量 count，用于限制输出元素的个数
   """
      0/ check parameter type
      1/ Counts the number of occurrences of each character in the parameter;
      2/ Returns an array in descending order of character frequency.
   """
   if type(string) == str:
      symbol_deleting_cn = ['~','！',"?","…",'，','。','：',"—","”","“"," ","「","」",'"',",","[","]","\n"]
      for x in symbol_deleting_cn:
         string = string.replace(x,'')
      string = [character for character in string]
      stats = dict([(character,string.count(character)) for character in string])
      c = Counter(stats)                                                         # /// day9 ///
      stats = c.most_common(count)                                               # /// day9 ///
   #  stats = sorted(stats.items(),key=lambda item:item[1],reverse=1)
      return stats
   else:
      raise ValueError(string)      

# 1.3 对中英文混杂的字符串进行再分类
def Reclassify_cn(string):
   """ Pick out Chinese characters in the string ”text“. """
   if type(string) == str:
      string_cn = string[:string.find("How")]
      return string_cn
   else:
      raise ValueError(string)

def Reclassify_en(string):
   """ Pick out English words in the string ”text“. """
   if type(string) == str:
      string_en = string[string.find("How"):]
      return string_en
   else:
      raise ValueError(string)


# 1.4 将统计中文字频和英文词频的函数封装为一个函数
def stats_text(string,count):
   """
      1/ Reclassify the string that mix Chinese characters and English words;
      2/ Counts the number of occurrences of each English word and each Chinese character in the parameter;
      3/ Returns an array in descending order of their frequency.
   """
   if type(string) == str:
      string_cn = Reclassify_cn(string)
      string_en = Reclassify_en(string)
      result_cn = stats_text_cn(string_cn,count)
      result_en = stats_text_en(string_en,count)
      print(result_en,"\n","\n","\n",result_cn)
   else:
      raise ValueError(string)
