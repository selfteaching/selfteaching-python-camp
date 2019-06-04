'''
1.创建一个名为d6_exercise_stats_word.py的文件

2.定义一个名为stats_text_en的函数，函数接受一个字符串text作为参数

3.实现该函数的功能（同day5任务2）：统计参数中每个英文单词出现的次数
最后返回一个按词频降序排列的数组

4.为Stats_text_en添加注释说明

'''

import re
def stats_text_en(text):  #定义函数
    text_1 = re.sub(r'[\W\u4e00-\u9fa5]',' ',text) #不是字符的，都转换为空格。主要去除标点符号
    text_1 = text_1.lower() #转换为小写
    textlist_1 = text_1.split()#将段落转换为列表
    dict1 = {} 
    for i in textlist_1:
        num= textlist_1.count(i)
        r1 = {i:num}
        dict1.update(r1)
        dict2=sorted(dict1.items(),key = lambda dict_items:dict_items[1], reverse=True)
    return(dict2)



#coding:utf-8
'''
封装统计中文汉字字频的函数
1.在d6_excercise_stats_word.py中定义一个名为stats_text_cn的函数，函数接受一个
  字符串text作为参数

2.实现该函数的功能：统计参数中每个中文汉字出现的次数，最后返回一个按字频降序排列的数组

3.为stats_text_cn添加注释说明

'''


def stats_text_cn(text):#设定函数
    word_dict = {} #定义一个空字典，作为结果容器
    cn_list = list(text) #将文本直接拆分为列表
    for s in cn_list: #统计中文汉字个数，并将结果返回word_dict中
      if '\u4e00'<= s <= '\u9fff':
        count=cn_list.count(s)
        r1={s:count}
        word_dict.update(r1)
    word_sorted = sorted(word_dict.items(), key=lambda items:items[1],reverse=True) #按字频降序排列输出结果
    return word_sorted



def stats_text(text):
  stats_dict = stats_text_cn(text) + stats_text_en(text) #合并中文汉字、英文单词统计结果并按频次倒序排列
  return stats_dict




