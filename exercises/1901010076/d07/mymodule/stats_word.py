# 作者：邓超
# 作业：合并中英文词频统计

import re   # 调用正则表达式模块，
          # re.sub(pattern, repl, string, count = 0,flags = 0)
def stats_text_en(text_en):  # 定义函数

    a = text_en.replace(',', '').replace('.', '').replace(':', '')  #去除符号
    a = a.replace('"', '').replace('!', '').replace('?', '').replace('_', '')   #去除符号
    a = a.lower()     #全英文单词小写
    a = re.sub("[^A-Za-z]", " ", a) #借用这个正则表达式，这里保留了英语单词，^代表取出大小写a-z以外所有的字符串剔除
    a = a.split()  # 分割字符串
    b = {}
    for i in a:
        count = a.count(i)
        r1 = {i: count}
        b.update(r1)
    c = sorted(b.items(), key=lambda x: x[1], reverse=True)
    print('英文单词统计词频如下：\n', c)    #这里print()函数缩进就是封装进我定义的函数里面去了
#中文词频统计
def stats_text_cn(text_cn):
    d = text_cn.replace('，', '').replace('、', '').replace('。', '').replace('：', '').replace('！', '').replace('？', '').replace(' ', '').replace('_', '')
    d = d.replace('\n', '').replace('.', '').replace('"', '').replace('?', '').replace('“”', '').replace('_', '').replace('!', '').replace(',', '').replace("'", '')
    d = re.sub("[A-Za-z0-9]", "", d)  #借用了这个正则表达式，这里删除了英文单词，因为没有加上^
    e = {}
    for j in d:
        count = d.count(j)
        r2 = {j: count}
        e.update(r2)
    f = sorted(e.items(), key=lambda x: x[1], reverse=True)
    print('中文单字统计词频如下：\n', f)

def stats_text(en_cn):
    text_list = stats_text_en(en_cn)
    text_list = stats_text_cn(en_cn)
    return text_list

#stats_text() 这个函数可以统计中文和英语的词频，并按照降序排列，



