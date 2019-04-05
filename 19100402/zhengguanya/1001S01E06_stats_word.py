#封装统计英文单词词频的函数
# 1.创建一个名为1001SO1E06_statas_word.py的文件
# 2.定义一个名为stats_text_en的函数，函数接受一个字符串text作为参数
# 3.实现该函数的功能(同days任务2):统计参数中每个英文单词出现的次数，最后返回一个按词频降序排列的数组
# 4.为stats_text_en添加注释说明

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

text = '''The Zen of Python, by Tim Peters
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
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

import re  
import collections  

symbol_deleting = [',','.','!','-','*','\'']  # 将非词类字符均替换为空格
for x in symbol_deleting:
   text = text.replace(x,'')
text = text.lower()                      # 将所有单词改为小写
text = text.split()                      # 将str转换为list
type(text)
print('我是分隔符')

def stats_text_en(word):
       result = {}
       for word in list(text):
         if  word not in result:
                result[word]=0
         result[word]+=1
       return result


def sort_by_count(d):  
    #字典排序  
    d = collections.OrderedDict(sorted(d.items(), key = lambda t: -t[1]))  
    return d  
  
if __name__ == '__main__':  
    file_name = list(text)  
  
    dword = stats_text_en(file_name)  
    dword = sort_by_count(dword)  
      
    for key,value in dword.items():  
        print(key + ":%d" % value)

   



                    

