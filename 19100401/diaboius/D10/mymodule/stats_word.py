import re
import jieba
from collections import Counter
#创建一个名为stats_text_en的函数
#使用字典（dicict）统计字符串样本text中各个英文单词出现的次数

def stats_text_en(en):
  '''统计单词字频'''
  if type(en)!=type("hello world"):#测试传入参数是否为字符串
      raise ValueError("this is not a str of correct type")
  else:
      result = re.sub("[^A-Za-z]", " ",en.strip())
      cnt=Counter(result.split()).most_common(100)   
      return cnt

#创建一个名为stats_text_cn的函数，功能：统计每个中文汉字出现的次数
def stats_text_ch(ch):
  '''统计词频 
    '''
  if type(ch)!=type("hello world"):#测试传入参数是否为字符串
      raise ValueError("this is not a str of correct type")
  else:
    #print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
    for i in ch:
      if u'\u4e00' <= i <= u'\u9fa5':   #提取中文汉字   \u是unincode编码，u4e00是十六进制表达值
        seg_list = jieba.cut(ch, cut_all=False)
  cut_words=[x for x in seg_list if len(x)>=2]
  return Counter(cut_words).most_common(20)
        
  
def stats_text(text):
  "统计合并英汉字频"
  if type(text)!=type("hello world"):#测试传入参数是否为字符串
      raise ValueError("this is not a str of correct type")
  else:
      return stats_text_en(text),stats_text_ch(text)
#print('**********************************************')
#print("按照出现次数从大到小输出所有的汉字及出现的次数")
#print('**********************************************'
#print (sorted(frequency.items(), key=lambda frequency: frequency[1],reverse=True))

