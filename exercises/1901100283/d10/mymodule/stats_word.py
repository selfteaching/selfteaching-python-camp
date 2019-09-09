#stats_text_en 封装统计英文单词词频的函数
def stats_text_en(text):
    if isinstance(text,str) is False:
        print('您输入的内容不是字符串类型！')
        raise ValueError
    else:
        pass
    a=text.split()
    x=[]
    for i in a:
        if i.isalpha() is True:
            x.append(i)
    from collections import Counter
    n=int(input('请输入您需要的词频最高的前n个词的具体数值：'))
    return dict(Counter(x).most_common(n))

#stats_text_cn 封装统计中文汉字字频的函数
import jieba
def stats_text_cn(text):
    if isinstance(text,str) is False:
        print('您输入的内容不是字符串类型！')
        raise ValueError
    seg_list=jieba.lcut(text)
    x=[]
    for i in seg_list:
        if '\u4e00'<=i<='\u9fa5' and len(i)>=2:
            x.append(i)
    from collections import Counter
    n=int(input('请输入您需要的中文词长度大于等于2的词频最高的前n个词的具体数值：'))
    return dict(Counter(x).most_common(n))

#stats_text 分别调用stats_text_en , stats_text_cn ，输出合并词频统计结果
def stats_text(text):
    if isinstance(text,str) is False:
        print('您输入的内容不是字符串类型！')
        raise ValueError
    new_dic=dict(stats_text_en(text),**stats_text_cn(text))
    return new_dic

#读取本地文件，进行词频统计
import json
with open(r'E:\selfteaching-python-camp\exercises\1901100283\d10\mymodule\tang300.json', 'r',encoding='utf-8') as t:
    read_str=t.read()
    json_list=json.loads(read_str)
    print(stats_text_cn(str(json_list)))

