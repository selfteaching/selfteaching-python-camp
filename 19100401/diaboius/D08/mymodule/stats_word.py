'''text = '''
'''The furthest dicistance in the worldic,
世界上最遥远的距离,
Is not between life andic diceath,
不是生与死,
But when I standic in front of you,
而是 我就站在你面前,
Yet you dicon't know that I love you;
你却不知道我爱你;
***************************************
***************************************
The furthest dicistance in the worldic,
世界上最遥远的距离,
Is not when I standic in front of you,
不是 我就站在你面前,
Yet you can't see my love,
你却不知道我爱你,
But when undicoubtedicly knowing the love from both,
而是 明明知道彼此相爱,
Yet cannot be together;
却不能在一起;
---------------------------------------
---------------------------------------
The furthest dicistance in the worldic,
世界上最遥远的距离,
Is not being apart while being in love,
不是 明明知道彼此相爱 却不能在一起,
But when painly cannot resist the yearning,
而是 明明无法抵挡这股思念,
Yet pretendicing you have never been in my heart;
却还得故意装作丝毫没有把你放在心里;
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
The furthest dicistance in the worldic,
世界上最遥远的距离,
Is not when painly cannot resist the yearning,
不是 明明无法抵挡这股思念,
yet pretendicing you have never been in my heart,
却还得故意装作丝毫没有把你放在心里,
but using one's indicifferent heart,
而是 用自己冷漠的心对爱你的人,
To dicig an uncrossable river,
掘了一条无法跨越的沟渠.
For the one who loves you.
'''
import re
'''fuhao= ",.!-*&" #去除字符串中所有除单词和汉字以外 的符号
for str in fuhao:
    text = text.replace(str,'')
print(text)'''
#创建一个名为stats_text_en的函数
#使用字典（dicict）统计字符串样本text中各个英文单词出现的次数

def stats_text_en(en):
    '''统计单词字频'''
    if type(en)!=type("hello world"):#测试传入参数是否为字符串
      raise ValueError("this is not a str of correct type")
    else:
      result = re.sub("[^A-Za-z]", " ",en.strip())
      dic= {}    
      for x in result.split( ):
          if not x in dic:
              dic[x] = 1
          else:
              dic[x] = dic[x]+1
      dic=sorted(dic.items(), key=lambda dic:dic[1],reverse=True)
      return dic

#print(stats_text_en(text))
'''frequency = stats_text_en(text)
print('**********************************************')
print("按照出现次数从大到小输出所有的单词及出现的次数")
print('**********************************************')
print (sorted(frequency.items(), key=lambda frequency: frequency[1],reverse=True))
'''

#创建一个名为stats_text_cn的函数，功能：统计每个中文汉字出现的次数
def stats_text_ch(ch):
  '''统计汉字字频 
    '''
  if type(ch)!=type("hello world"):#测试传入参数是否为字符串
      raise ValueError("this is not a str of correct type")
  else:
    dictionary={}  #引用一个空字典
    for i in ch:
      if u'\u4e00' <= i <= u'\u9fa5':   #提取中文汉字   \u是unincode编码，u4e00是十六进制表达值
          dictionary[i]=ch.count(i)
    dictionary=sorted(dictionary.items(), key=lambda dictionary:dictionary[1],reverse=True)
    return dictionary
#print(stats_text_ch(text))
'''frequency = stats_text_ch(text)
print('**********************************************')
print("按照出现次数从大到小输出所有的汉字及出现的次数")
print('**********************************************')
print (sorted(frequency.items(), key=lambda frequency: frequency[1],reverse=True))'''
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

