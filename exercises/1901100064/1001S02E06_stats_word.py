
# 统计英文单词数量
def stats_text_en(text):
  elements=text.split()
  words=[]
  symbols=',.*-!'

  for element in elements:
    for symbol in symbols:
      element=element.replace(symbol,'')
    if len(element):
      words.append(element)

  counter={}
  words_set=set(words)

  counter={word:words.count(word) for word in words_set}
  return sorted(counter.items(),key=lambda x:x[1],reverse=True)


###################################################################################
# 统计中文汉字数量

def stats_text_cn(text):

  cn_characters = []

  for character in text:
    if '\u4e00'<=character<='\u9fa5':
      cn_characters.append(character)
  
  counter = {}
  cn_counter_set = set(cn_characters)
  
  for character in cn_counter_set:
    counter[character]=cn_characters.count(character)

 
  return  sorted(counter.items(),key=lambda x:x[1],reverse=True)


##########################################################################################

en_text= '''The Zen of   Python , by Tim Peters 
  Beautiful is better than ugly.
  Explicit is better than implicit. 
  Simple is better than complex. 
  Complex is better than complicated.
  Flat is better than nested. 
  Sparse is better than dense. 
  Readability counts. 
  Special cases aren't special enough to break the rules. 
  Although practicality beats purity. Errors should never pass silently. 
  Unless explicitly silenced. In the face of ambxiguity, refuse the temptation to guess. 
  There should be one-- and preferably only one --obvious way to do it. 
  Although that way may not be obvious at first unless you're Dutch. 
  Now is better than never. Although never is often better than *right* now. 
  If the implementation is hard to explain, it's a bad idea. 
  If the implementation is easy to explain, it may be a good idea. 
  Namespaces are one honking great idea -- let's do more of those!
  '''

cn_text= '''
python 之禅 by Tim Peters

优美胜于丑陋
明了胜于晦涩
简洁胜于复杂
扁平胜于嵌套
间隔胜于紧凑
可读性很重要
即便假借特例的实用性之名，也不可违背这些规则
不要包容所有错误，除非你确定需要这样做
当存在多种可能时，不要尝试去猜测
而是尽量找一种，最好是唯一一种明显的解决的方案
虽然这并不容易，因为你不是python之父
做也许好过不做，但不假思索就动手还不如不做
，，，，
。。。。


'''


if __name__ == '__main__' :
  en_result = stats_text_en(en_text)
  cn_result = stats_text_cn(cn_text)
  print('统计参数中每个英文单词出现的次数==》\n',en_result)
  print('统计参数中每个中文单词出现的次数==》\n',cn_result)

