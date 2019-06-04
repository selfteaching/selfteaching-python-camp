textt = '''
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
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
自从20世纪90年代初Python语言诞生至今，它已被逐渐广泛应用于系统管理任务的处理和Web编程。
'''
import collections
import re
def stats_textt_en(textt_en):
# 统计每个英文单词出现的次数
# 第一步：过滤英文字符，并将text拆分为list
# 第二步：清理*-等标点符号
# 第三步：使用collections库中的counter函数进行词频统计结果。
    result = re.sub("[^A-Za-z]","",textt_en.strip())
    newList = result.split()
    x=0
    for x in range(0,len(newList)):
        newList[x]=newList[x].strip("*-,.?!")
        if newList[x]=="":
            newList[x].remove('')
        else:
                x+=1
    print("英文单词次品统计结果：",collections.counter(newList),"\n")




def stats_textt_cn(textt_cn):
# 统计每个汉字出现的次数
# 第一步：过滤汉字字符，并定义频率统计函数 stats()。
# 第二步：清除文本中的标点字符,将非标点字符组成新列表 new_list。
# 第三步：遍历列表，将字符同上一次循环中频率统计结果作为形参传给统计函数stats()。
#  第四步：统计函数在上一次统计结果基础上得出本次统计结果，赋值给newDict。
# 第五步：new_list遍历结束，输出倒序排列的统计结果。
    result1 = re.findall(u'[\u4e00-\u9fff]+', textt_cn)
    newtextt = ''.join(result1)

    def stats(orgtextt, newDict) :
        d = newDict
        for m in orgtextt :
            d[m] = d.get(m, 0) + 1
        return d
    
    new_list = []
    for char in newtextt :
        cn = char.strip('-*、。，：？！……')
        new_list.append(cn)

    words = dict()
    for n in range(0,len(new_list)) :
        words = stats(new_list[n],words)
    newWords = sorted(words.items(), key=lambda item: item[1], reverse=True) 
    print('中文汉字字频统计结果： ',dict(newWords))

# 调用函数
    stats_textt_en(textt)
    stats_textt_cn(textt)

