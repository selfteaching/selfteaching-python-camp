text = [2,3,4,5]
import re
import collections
def stats_text_cn(text):
    if type(text)!= str:
        raise ValueError("文本必须是字符串")
    p=re.compile(u'[\u4e00-\u9fa5]') #匹配一组字符可以用方括号[]定义自己的字符分类。
    a=re.findall(p,text)  #找到text中匹配中文u'[\u4e00-\u9fa5]'
                          #re.findall遍历匹配，可以获取字符串中所有匹配的字符串，返回一个列表。            
    str=''.join(a) # ''.join()是字符串操作函数，常常用于字符连接操作。把list列表转为str字符串
    print(collections.Counter(str)) #统计中文词频

def stats_text_en(text):
    if type(text)!= str:
        raise ValueError("文本必须是字符串")
    b=re.sub(r'[^A-Za-z]',' ',text) #用正则表达式过滤出26个大小写英文字母。text中非字母的替换成空格。
    list=b.split() #以空格分割，返回分割后字符串列表。
    print(collections.Counter(list)) #统计单词词频

def stats_text(text):    
    if type(text)!= str:
        raise ValueError("文本必须是字符串") 
    stats_text_cn(text)
    stats_text_en(text)
 

stats_text(text)