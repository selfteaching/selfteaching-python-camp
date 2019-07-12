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
      2/ Returns an dictionary in descending order of word frequency.
   """
   if type(string) == str:
      # ------------------- 剔除所有符号，并将所有中文字符替换成空格 ------------------- #
      string = re.sub('[\s+\.\!\/_,$%^*(+\"\'\?]+|[+——！，。？、~@#￥%……&*（）“”‘’：《》［ ］「」-]+', '', string)
      for x in string:
         if ord(x)>=256:
            string = string.replace(x," ")
      string = string.split()
      # ----------------------------- 创建计数器，并排序 ---------------------------- #
      c = Counter(string)
      stats = dict(c.most_common(count))
      return stats
   else:
      raise ValueError(string)

# 1.2 封装统计中文汉字字频的函数
def stats_text_cn(string,count):
   """
      0/ check parameter type
      1/ Counts the number of occurrences of each character in the parameter;
      2/ Returns an dictionary in descending order of character frequency.
   """
   if type(string) == str:
      # -------------------------- 剔除所有英文单词和标点符号 ------------------------ #
      string = re.sub(r'[a-zA-Z]+|[0-9]+', '', string)
      string = re.sub('[\s+\.\!\/_,$%^*(+\"\'\?]+|[+——！，。？、~@#￥%……&*（）“”‘’：《》［ ］「」-]+', '', string)
      # ------------------------------------------------------------------------- #
      seg_list = jieba.lcut(string)       # 直接返回分词完毕的列表seg_list
      seg_dic = dict([(word,seg_list.count(word)) for word in seg_list if len(word)>=2]) # 遍历seg_list，生成词典seg_dic，该词典的”key“长度均 >=2
      c = Counter(seg_dic)                # 创建计数器 c
      stats = dict(c.most_common(count))  # 返回一个列表stats，该列表包含了count个最常见元素和它们对应的值
      return stats
   else:
      raise ValueError(string)      

# 1.3 将统计中文字频和英文词频的函数封装为一个函数
def stats_text(string,count):
   """
      1/ Counts the number of occurrences of each English word and each Chinese character in the parameter;
      2/ Combine "result_cn" and "result_en" into dictionary "dict_Merged";
      3/ Returns an array "stats" in descending order of word frequency.
   """
   if type(string) == str:
      result_cn = stats_text_cn(string,count)
      result_en = stats_text_en(string,count)
      dict_Merged = dict(result_cn, **result_en)
      stats = Counter(dict_Merged).most_common(count)
      return stats
   else:
      raise ValueError(string)