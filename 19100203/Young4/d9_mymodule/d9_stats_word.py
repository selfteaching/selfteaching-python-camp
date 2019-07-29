import re, collections
def stats_text_en(text,count):  #定义函数
  if isinstance(text,str) == True:
    text_1 = re.sub(r'[\W\u4e00-\u9fa5]',' ',text) #不是字符的，都转换为空格。主要去除标点符号
    text_1 = text_1.lower() #转换为小写
    textlist_1 = text_1.split()#将段落转换为列表
    dict1 = collections.Counter(textlist_1).most_common(count)
    
    return(dict1)
  else:
    raise ValueError('输入参数无效，请输入字符串类型参数')



#coding:utf-8
'''
封装统计中文汉字字频的函数
1.在d6_excercise_stats_word.py中定义一个名为stats_text_cn的函数，函数接受一个
  字符串text作为参数

2.实现该函数的功能：统计参数中每个中文汉字出现的次数，最后返回一个按字频降序排列的数组

3.为stats_text_cn添加注释说明

'''


def stats_text_cn(text,count):#设定函数
  if isinstance(text,str):   
    word_dict = {} #定义一个空字典，作为结果容器
    cn_list = list(text) #将文本直接拆分为列表
    for s in cn_list: #统计中文汉字个数，并将结果返回word_dict中
      if '\u4e00'<= s <= '\u9fff':
        count1=cn_list.count(s)
        r1={s:count1}
        word_dict.update(r1)     
    return collections.Counter(word_dict).most_common(count)
    
  else:
    raise ValueError('输入参数无效，请输入字符串类型参数')



def stats_text(text,count):
  if isinstance(text,str) == True:
    stats_dict = stats_text_cn(text,count) + stats_text_en(text,count) #合并中文汉字、英文单词统计结果并按频次倒序排列
    return stats_dict
  else:
    raise ValueError('输入参数无效，请输入字符串类型参数')