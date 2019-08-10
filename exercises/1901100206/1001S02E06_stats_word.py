Poetry='''
Right here waiting for you—Richard Marx（USA）
ocean apart day after day
and i slowly go insane
i hear your voice on the line
but it doesn't stop the pain
if i see you next to never
how can we say forever
wherever you go
whatever you do
i will be right here waiting for you
whatever it takes
or how my heart breaks
i will be right here waiting for you
i took for granted, all the times
that i thought would last somehow
i hear the laughter, i taste the tears
but i can't get near you now
oh, can't you see it baby
you've got me going crazy
wherever you go
whatever you do
i will be right here waiting for you
whatever it takes
or how my heart breaks
i will be right here waiting for you
i wonder how we can survive
this romance
but in the end if i'm with you
i'll take the chance
oh, can't you see it baby
you've got me going crazy
wherever you go
whatever you do
i will be right here waiting for you
whatever it takes
or how my heart breaks
i will be right here waiting for you
waiting for you
'''
#英文字符排序
import string #要调用string.punctuation函数
def stats_text_en(text):
    text_1 = text.lower().split()
    text_2 = []
    dic = {}        
    for elem in text_1:
        for sym in string.punctuation:  #string.punctuation函数找出所有标点符号等
            elem = elem.replace(sym, '')  #对text_1逐个剔除标点符号
        text_2.append(elem)   #清洗后的数据重新组成列表
    for key in set(text_2):   
#        if text_2.count(key) > 0:     #上次作业有这行代码，不加不影响结果
            dic[key] = text_2.count(key)  #给text_2的键逐个计数，并储存它的值。
    dic_1 = sorted(dic.items(), key=lambda x: x[1], reverse=True) #reverse=True代表降序
    return dic_1 #上行代码：.items()将字典转换成元组，lambda x: x[1]配合sorted()使用时代表用x[1]的值排序
print(stats_text_en(Poetry))


Principle='''
原则是能够在相似场景下反复运用的一套概念，有别于具体问题的狭义回答。
每个游戏的获胜者都有自己遵循的原则，生活也是如此。原则是应对自然或生活规律的种种方式。
对原则理解越透彻，越能在生活中游刃有余。
生活的不同方面也有各自的原则，例如滑雪有“滑雪原则”，做父母的有“父母原则”，
管理有“管理原则，投资有“投资原则”等等，也存在支配一切，包罗万象的“生活原则”。
当然每个人都有自己认为最有效的原则。
'''
#中文字符排序
def stats_text_cn(text):
    import re
    dic = {}
    cn = re.findall(r'[\u4E00-\u9FFF]', text) #\u4E00-\u9FFF代表取出中文字符
    #print(cn)  #上一步得到的结果中便不含各种标点符号
    #省下去除标点符号这一步骤
    for char in set(cn):   #作用同上面英文排序
        dic[char] = cn.count(char)
    dic_1 = sorted(dic.items(), key=lambda x: x[1], reverse=True) 
    return dic_1   
    #最后这段为借鉴：
    #加上后能让结果竖屏显示，但需要去除上行代码，及去除执行该函数的print()
    #print('字符\t字频')
    #print('============')
    #for sym in dic_1:
    #    print('%s\t%d'%sym)

print(stats_text_cn(Principle))

#总结：
#正如python之禅里说：Simple is better than complex.
#所以对于做作业，我都会想着用更短，更少的代码去得到同样的结果