import collections
import re
import jieba
def stats_text_en(en,count):  
    '''英文词频统计'''
    '''参数类型检查；如果输入参数不为字符串则抛出ValueError'''
    if type(en)== str: # 判断输入的是字符，执行以下语句

         text_en = re.sub("[A-Za-z]"," ", en.strip()) #只保留字母，并用空格作为分隔符
         enlist=text_en.split() #以空格和折行为分隔，将每个被分割的内容作为一个列表的元素，并将所有列表元素和在一起，组成一个列表
         return collections.Counter(enlist).most_common(count)
         #利用coletions中的counter为每个出现的英文单词计数，返回前count个词频最高的词及出现的次数
    else:
         raise ValueError("输入的不是字符串")   

def stats_text_cn(cn,count):
    '''中文汉字字频统计'''
    '''参数类型检查；如果输入参数不为字符串则抛出ValueError'''    
    if type(cn)== str: # 判断输入的是字符，执行以下语句

         text_cn = re.findall(u'[\4e00-\u9fff]+',cn.strip()) #只保留字母，并用空格作为分隔符
         cnlist=text_cn.split() #以空格和折行为分隔，将每个被分割的内容作为一个列表的元素，并将所有列表元素和在一起，组成一个列表
         seg_list = jieba.cut(' '.join(cnlist))
         cn1 = []
         for i in seg_list:
              if len(i) >= 2:
                   cn1.append(1)
         return collections.Counter(cnlist).most_common(count)
                        #利用coletions中的counter为每个出现的中文汉字计数，返回前count个词频最高的词及出现的次数
    else:
         raise ValueError("输入的不是字符串")   

def stats_text(text_e_c,count_e_c):
    '''合并英汉词频统计'''
    '''参数类型检查，如果输入参数不为字符串则抛出ValueError'''
    if type(text_e_c) == str:
         return(stats_text_en(text_e_c,count_e_c)+stats_text_cn(text_e_c,count_e_c))
    else:
         raise ValueError("输入的不是字符串")
        
# encoding=utf 
import jieba #day10
import collections

# 函数1：统计输入文本中英文单词的词频：
def stats_text_en(text,count):
    if not isinstance(text,str):
        raise ValueError('输入的不是文本格式，请重新输入：') # 第8天作业要求，添加参数类型检查
    text = text.replace('.', '').replace('!', '').replace('--', '').replace('*', '').replace(',', '').replace('(', '').replace(')', '').replace(';', '').replace(':', '').replace('\'', '').replace('?', '').replace('_', '').replace('-', '').replace('/', '') .replace('[', '') .replace(']', '') .replace('\\', '') .replace('\"', '').replace('{', '').replace('}', '').replace('\t', '').replace('\n', '').replace('\r\n', '')    
        
    # 以上替换去除各种标点符号
    list_text = text.split() # 将字符串转换为列表
    import collections
    count = int(input("请输入要限制输出的元素个数："))
    dic = collections.Counter(list_text).most_common(count)
    return dic



# 函数2：统计输入文本中中文字的词频：
def stats_text_cn(text):  
    if not isinstance(text,str):
        raise ValueError('输入的不是文本格式，请重新输入：') # 第8天作业要求，添加参数类型检查
    
    text1 = []
    for i in text:  # 这个循环有效，说明一串汉字也是一个字符串，每个汉字就是其中的一个元素，可以用for in 来遍历，其中i代表了每个汉字的unicode编码
        if u'\u4e00' > i > u'\u9fff':     # 挑选出非中文字
            text=text.split(i,"") # 将非中文字符替换
    seg_list = jieba.cut(text,cut_all =False) 
    
    for j in seg_list:
             if len(j) >= 2 : #只统计长度大于等于2的词
              text1.append(j)
    count = int(input('请输入要限制输出的元素个数：'))
    text1 = collections.Counter(text1).most_common(count)  #按出现次数从大到小排列
    return text1


# 函数3：统计中英文混合词频：
def stats_text(text) :
    '''合并中英文词频'''
    '''参数类型检查，如果输入参数不为字符串抛出ValueError'''
    if  not  isinstance(text, str) :
        return(stats_text_en(text) + stats_text_cn(text))
    else:
        raise ValueError("输入的不是字符串")

# print(stats_text(text))

print(stats_text.__doc__)
          
