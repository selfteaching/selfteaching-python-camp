# 一、将统计中文字频和英文词频的函数封装为一个模块
# 1、添加一个名为 stats_text 的函数，实现功能：分别调用 stats_text_en, stats_text_cn，输出合并词频统计结果

from collections import Counter                                                  # /// day9 ///
import jieba
import re

# 1.1 封装统计英文单词词频的函数
def stats_text_en(string,count):                                                 # /// day9 /// 添加int类型变量 count，用于限制输出元素的个数
   """
      0/ check parameter type
      1/ Counts the number of occurrences of each word in the parameter;
      2/ Returns an array in descending order of word frequency.
   """
   if type(string) == str:
      string = ''.join(x for x in string if ord(x) < 256)
      string = string.lower()
      string = string.split()
      for i in range(len(string)):
         string[i] = string[i].strip(',-*!.?')
      c = Counter(string)
      stats = dict(c.most_common(count))
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
      string = re.sub(r'[a-zA-Z]+|[0-9]+', '', string)
      string = re.sub('[\s+\.\!\/_,$%^*(+\"\'\?]+|[+——！，。？、~@#￥%……&*（）“”‘’：《》［ ］「」-]+', '', string)
      seg_list = jieba.lcut(string)                                                      # /// day10 /// 直接返回分词完毕的列表seg_list
      seg_dic = dict([(word,seg_list.count(word)) for word in seg_list if len(word)>=2]) # /// day10 /// 遍历seg_list，生成词典seg_dic，该词典的”key“长度均 >=2
      c = Counter(seg_dic)                                                               # /// day10 /// 创建计数器 c
      stats = dict(c.most_common(count))                                                 # /// day9 ///  返回一个列表stats，该列表包含了count个最常见元素和它们对应的值
      return stats
   else:
      raise ValueError(string)      

# 1.3 将统计中文字频和英文词频的函数封装为一个函数
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