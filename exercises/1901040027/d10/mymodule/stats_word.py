
# stats_text module
import re
def stats_text_en(text, count): #在第八天基础上那个增加count控制输出
    from collections import Counter #调用Counter计算器
    if not isinstance(text, str):
        raise ValueError('input data is not string type!,again!')
    text = text.replace(',','').replace('.','').replace('--','').replace('*','').replace('!','')#讲非英文字符转化为空
    text = text.lower()#将所有英文字符改为小写
    text = text.split()#以空格拆分独立的单词
    #count = int(count) #增加一个int类型变量count
    dir1 = {}
    for i in text: #将字符转换为字典
        count = text.count(i)
        r1 = {i:count}
        dir1.update(r1)

    # dir2 = sorted(dir1.items(),key = lambda x:x[1],reverse = True)
    #dir2 = Counter(dir1).most_common(count) #按词频排序并用count控制输出
    #print(dir2)


import jieba
def stats_text_cn(text, count): #在第八天基础上那个增加count控制输出
    from collections import Counter #调用Counter计算器
    if not isinstance(text, str):
        raise ValueError('input data is not string type!')
    text = text.replace('\n','').replace('，','').replace('、','').replace(' ','').replace('""','')#删掉换行符，逗号，顿号,空格
    text = re.sub('[^\u4e00-\u9fa5]','',text)
    text = jieba.lcut(text)
    text1 =[]
    for i in text:
        if len(i) >= 2:
            text1.append(i)
    count = int(count) #增加一个int类型变量count
    #b1 = {} 
    #for i in text: #由字符生成字典
    #    b1.update({i: text.count(i)})

    #b2 = sorted(b1.items(),key = lambda x:x[1],reverse = True)
    b2 = Counter(text1).most_common(count) #按词频排序并用count控制输出
    print(b2)


def stats_text(text, count):
    from collections import Counter #调用Counter计算器
    if not isinstance(text, str):
        raise ValueError('input data is not string type!')
    stats_text_en(text, count) #统计英文单词
    stats_text_cn(text, count) #统计中文单词