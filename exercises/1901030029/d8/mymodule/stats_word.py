text='''
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
Unless explicitly silencedIn the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do itAlthough that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
去除英文单词中的标点符号
'''
import re
fuhao=",.!-*，。&"                         #去除英文单词中
for a in fuhao:
    text=text.replace(a,'')
print(text)


def stats_text_en(text):                   #定义一个以字符串text为参数的函数
    if not isinstance (text,str):
        raise ValueError ('字符串必须是str类型，输入类型  %s' %type(text))
    result=re.sub("[^A-Za-z]"," ",text.strip())#统计单词次数
    dic={}                                 #使用字典统计text中的每个英文单词出现的次数
    for x in result.split():
        if not x in dic:
            dic[x]=1
        else:
            dic[x]=dic[x]+1
    return dic
frequency = stats_text_en(text)
print('******************************')
print("按照出现次数从小到大输出所有的单词及出现的次数")
print('******************************')
print(sorted(frequency.items(),key=lambda x:x[1],reverse=True))

 #创建一个名为stas_text_cn的函数 
def stats_text_cn(text):
    if not isinstance(text,str):
        raise ValueError('字符串必须是str类型，输入类型  %s' %type(text))
    dictionary={}                         #引用一个新字典
    for i in text:
        if u'\u4e00' <= i <=u'\u9fa5':    #提取中文汉字 \u是unincode的编码，u4e00是十进制表达式
             dictionary[i]=text.count(i)
    return dictionary
frequency = stats_text_cn(text)
print('**************************')
print("按照出现次数从大到小输出所有的汉字以及出现的次数")
print('**************************')        
print(sorted(frequency.items(),key=lambda x: x[1],reverse=True))

def stats_text(text):
    '''分别调⽤stats_text_en , stats_text_cn ，输出合并词频统计结果'''
    if not isinstance(text,str):
        raise ValueError('字符串必须是str类型，输入类型  %s' %type(text))

    return  stats_text_en(text).update(stats_text_cn(text))
    # print(result)
    # return result