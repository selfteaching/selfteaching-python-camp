import re
import jieba
from collections import Counter

def stats_text_en(text,count):
    if type(text)==str:
        edit_text = re.sub("[^A-Za-z]", " ", text)
        edit_text = edit_text.split()

    else:
        raise ValueError ('type of argumengt is not str')

    counter = Counter(edit_text).most_common(count)
    counter = dict(counter)
    #print(counter)
    # for key in counter:#将数据按照格式化打印出来
    #     print("英文字符里这个：'{}'字符出现了{}次".format(key, counter[key]))

    a_dir = sorted(counter.items(),key=lambda x:x[1],reverse=True)
    #print(a_dir)
#上面这句话是将字典中的数据进行排序
    list = []
    for i in a_dir:#排序好之后遍历取出字符就好，数字就不要了
        list.append(i[0])#取出符合条件的字符加入新的列表
    return list#返回这个排序好之后的字符

# print('==============分割线===================')

def stats_text_cn(text,count):
    if type(text)==str:
        edit_text = re.compile(r'[\u4e00-\u9fa5]+')
        res = re.findall(edit_text,text)
        cnstr = ''.join(res)
    else:
        raise  ValueError ('type of argumengt is not str')

    after_jieba = jieba.cut(cnstr)
    tmp = []
    for i in after_jieba:
        if len(i)>1:
            tmp.append(i)

    counter = Counter(tmp).most_common(count)
    counter = dict(counter)
    # for key in counter:#将数据按照格式化打印出来
    #     print("中文字符里这个：'{}'字符出现了{}次".format(key, counter[key]))

    a_dir = sorted(counter.items(), key=lambda x: x[1], reverse=True)
# 上面这句话是将字典中的数据进行排序
    list5 = []
    for i in a_dir:#排序好之后遍历取出字符就好，数字就不要了
        list5.append(i[0])#取出符合条件的字符加入新的列表
    print(list5)
    return list5

#text = 'aaa,aaa,aaa,sdafasdf,sadfasdf,asdfsadf,你好,你好,你好,世界'
def stats_text(text,count):#将两个函数做成一个函数
    if type(text)==str:
        return stats_text_en(text,count) + stats_text_cn(text,count)
    else:
        raise ValueError ('type of argumengt is not str')


#stats_text()#调用