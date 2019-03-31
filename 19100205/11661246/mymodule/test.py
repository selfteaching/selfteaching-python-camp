import jieba
import collections
# 函数2：统计输入文本中中文字的词频：
def stats_text_cn(text):  
    if not isinstance(text,str):
        raise ValueError('输入的不是文本格式，请重新输入：') # 第8天作业要求，添加参数类型检查
    
    text1 = []
    for i in text:  # 这个循环有效，说明一串汉字也是一个字符串，每个汉字就是其中的一个元素，可以用for in 来遍历，其中i代表了每个汉字的unicode编码
        if i <u'\u4e00' or > u'\u9fff':     # 挑选出非中文字
            text=text.split(i,"") # 将非中文字符删除
    seg_list = jieba.cut(text,cut_all =False)
    
    for j in seg_list:
             if len(j) >= 2 : #只统计长度大于等于2的词
              text1.append(j)
    count = int(input('请输入要限制输出的元素个数：'))
    text1 = collections.Counter(text1).most_common(count)  #按出现次数从大到小排列
    return text1
    
with open('tang300.json','r',encoding='UTF-8') as f:
    a = f.read()
try:
    if not isinstance(a,str):
        raise ValueError()
    
except ValueError:
    print('输入的不是文本格式，请重新输入：')   
    
print(stats_text_cn(a))