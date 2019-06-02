import re
import jieba
from collections import Counter
#创建一个名为stats_text_en的函数
#使用字典（dicict）统计字符串样本text中各个英文单词出现的次数

def stats_text_en(en,count):
  '''统计单词字频'''
  if type(en)!=type("hello world"):#测试传入参数是否为字符串
      raise ValueError("this is not a str of correct type")
  else:
      result = re.sub("[^A-Za-z]", " ",en.strip())
      cnt=Counter(result.split()).most_common(count)   
      return cnt

#创建一个名为stats_text_cn的函数，功能：统计每个中文汉字出现的次数
def stats_text_cn(ch,count):
  '''统计词频 
    '''
  if type(ch)!=type("hello world"):#测试传入参数是否为字符串
    raise ValueError("this is not a str of correct type")
  else:
     ch=re.sub('[^\u4e00-\u9fa5]','',ch)
     ch=[x for x in jieba.cut_for_search(ch.strip()) if len(x)>=2]   
     return Counter(ch).most_common(count)
        
  
def stats_text(text,count):
  "统计合并英汉字频"
  if type(text)!=type("hello world"):#测试传入参数是否为字符串
      raise ValueError("this is not a str of correct type")
  else:
      return stats_text_en(text,count),stats_text_cn(text,count)
#print('**********************************************')
#print("按照出现次数从大到小输出所有的汉字及出现的次数")
#print('**********************************************'
#print (sorted(frequency.items(), key=lambda frequency: frequency[1],reverse=True))

