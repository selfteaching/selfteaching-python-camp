# this is d6 excercise for defining functions
# date : 2019.3.23
# author by : qiming

# 示例字符串
string1 = '**an apple is an apple,  --fruite is fruite, **apple is kind of fruite or not...'
string2 = '苹果是不是水果？-- 可能是，也可能不是。'

import collections

def stats_text_en(string_en):
    ''' 统计英文词频
    
    第一步：将string拆分为list。
    第二步：清理*-等标点符号。
    第三步：使用collections库中的Counter函数进行词频统计并输出统计结果。
    '''
    newList = string_en.split( )
    i=0
    for i in range(0,len(newList)):
        newList[i]=newList[i].strip('*-,.?!')
        if newList[i]==' ': 
            newList[i].remove(' ')
        else:
            i=i+1
    print(collections.Counter(newList))

def stats_text_cn(string_cn):
    ''' 统计中文汉字字频
    
    第一步：定义频率统计函数 stats()。
    第二步：清除文本中的标点字符,将非标点字符组成新列表 new_list。
    第三步：遍历列表，将字符同上一次循环中频率统计结果作为形参传给统计函数stats()。
    第四步：统计函数在上一次统计结果基础上得出本次统计结果，赋值给newDict。
    第五步：new_list遍历结束，输出倒序排列的统计结果。
    '''
    def stats(orgString, newDict) :
        d = newDict
        for m in orgString :
            d[m] = d.get(m, 0) + 1
        return d

    new_list = []
    for char in string_cn :
        cn = char.strip('-*、。，：？！……')
        new_list.append(cn)
    
    words = dict()
    for n in range(0,len(new_list)) :
        words = stats(new_list[n],words)
    #print(words)
    newWords = sorted(words.items(), key=lambda item: item[1], reverse=True) 
    print(dict(newWords))  

# 调用函数
stats_text_en(string1)
stats_text_cn(string2)

