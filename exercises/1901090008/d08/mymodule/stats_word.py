text = '''
The Zen of python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases arent't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced
In the face of ambxiguity,refuse the temptation to guess
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch
If the implementation is hard to explain,it's a bad idea
If the implementation is easy to explain,it's may be a good idea.
Namespaces are one honking great idea --let's do more of those!
'''

def stats_text_en (text):  #定义：函数+括弧，为函数添加注释，
    if not isinstance(text,(str)):   #参数检查
        raise ValueError('bad operand type')   #抛出错误

    replace_text = text.replace(',',' ').replace('.',' ').replace('--','').replace('!','').replace('*',' ').replace('\n','')  #第一步：去掉标点符号
    lower_text = replace_text.lower()          #第二步：单词全改为小写/大写
    split_text = lower_text.split()         #第三步：文本字符串拆分为用空格隔开的列表

    wordcount={}                               #第四步：创建空字典
    for i in split_text:                       #第五步：for语句从列表中取出单个单词
        if i not in wordcount:             #第六步：if循环判断？计数
            wordcount[i] = 1  #？,既然不在字典中，为何还会等于1呢？
        else:
            wordcount[i]+=1


    wordcount = sorted(wordcount.items(),key=lambda x:x[1],reverse=True) #第七步：dict= sorted(dict.items(),key=lambda x:x[1],reverse=True)字频从大到小顺序排列
    return wordcount


print(stats_text_en(text)) #用于测试



def stats_text_cn(text):
    if not isinstance(text,(str)):
        raise ValueError('bad operand type')


    text1 = text.replace('，' , ' ').replace('。' , ' ').replace('：' , ' ').replace('！' , ' ').replace('\n', ' ').replace('？', ' ')
    text2 = list(text1)             #汉字词频统计不需要空格符隔开

    dict = {}
    for i in text2:
        if '\u4e00' <= i <= '\u9fff': #找中文字符
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1

    dict =sorted(dict.items(), key =lambda x:x[1], reverse = True)
    return dict


print(stats_text_cn(text)) #用于测试


def stats_text(text):
    '''合并统计英文词频和中文词频'''
    if not isinstance(text,str):
        raise ValueError('bad operand type')

    print(stats_text_en(text)+stats_text_cn(text))
