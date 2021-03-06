#统计每个单词中英文出现的次数

import re
import jieba
from collections import Counter
#创建一个名为stats_text_en的函数
#使用字典（dicict）统计字符串样本text中各个英文单词出现的次数

def stats_text_en(text,count):
  '''统计单词字频'''
  if not isinstance(text, str):
                raise ValueError("This is not string!")
  else:
      result = re.sub("[^A-Za-z]", " ",en.strip())
      cnt=Counter(result.split()).most_common(count)   
      return cnt

#创建一个名为stats_text_cn的函数，功能：统计每个中文汉字出现的次数
def stats_text_cn(text,count):
  '''统计词频 
    '''
  if not isinstance(text, str):
                raise ValueError("This is not string!")
  else:
     cn=re.sub('[^\u4e00-\u9fa5]','',text)
     cn=[x for x in jieba.cut_for_search(text.strip()) if len(x)>=2]   
     return Counter(cn).most_common(count)
        
  
def stats_text(text,count):
  "统计合并英汉字频"
  if not isinstance(text, str):
                raise ValueError("This is not string!")
  else:
      return stats_text_en(text,count),stats_text_cn(text,count)
#print('**********************************************')
#print("按照出现次数从大到小输出所有的汉字及出现的次数")
#print('**********************************************'
#print (sorted(frequency.items(), key=lambda frequency: frequency[1],reverse=True))





en_text='''
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
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

cn_text='''
美丽胜过丑陋。
显式优于隐式。
简单比复杂更好。
复杂比复杂更好。
优于嵌套。
稀疏优于密集。
可读性很重要。
特殊情况不足以打破规则。
虽然实用性胜过纯洁。
错误不应该默默地传递。
除非明确沉默。
面对困惑，拒绝猜测的诱惑。
应该有一个 - 最好只有一个 - 明显的方法来做到这一点。
虽然这种方式起初可能并不明显，除非你是荷兰人。
现在比永远好。
虽然现在永远不会比*正确好。
如果实施很难解释，这是一个坏主意。
如果实现很容易解释，那可能是个好主意。
命名空间是一个很棒的主意 - 让我们做更多的事情吧！
'''

