import re # 调用正则表达式模块
t= '''
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
我爱你胜过你爱我，他那么爱你！你却爱着我。
'''
def stats_text_en(text):   #定义统计英文字符的函数
    
    for i in '.'',''-''*''!''?''。':      #利用for循环去掉标点符号
        text=text.replace(i,' ')
        
    text=text.lower()     #把字符串统一为小写字母
    t1= re.sub("[^A-Za-z]", " ", text)    # 利用正则表达式提取英文字符re.sub(pattern, repl, string, count=0, flags=0)
    counts={}                 #新建一个空字典
    t2=t1.split()             #拆分提取出来的英文字符串
    
    for i in t2:               #利用循环统计字符出现的次数
        count=t2.count(i)
        counts[i]=count
    countslist = list(counts.items())      #将字典转换为列表形式
    t2=sorted( countslist,key=lambda x:x[1],reverse=True)   #按字符出现次数的大小排列
    print(t2)
    t2=countslist.sort( key=lambda x:x[1],reverse=True)      #这一步是觉得好玩把字符和次数单独挑出来按大小一一对应排列
    for i in range(35):
        word,count=countslist[i]
        print('{0:<15}{1:<2}'.format(word,count))
            
def stats_text_cn(text):        #定义统计中文字符的函数
    t1=re.findall(r'[\u4e00-\u9fa5]',text)    #利用正则表达式按unicode编码将中文提取出来
    counts={}                    #新建一个空字典
    for i in t1:                 #利用循环统计中文字符出现的次数
        count=t1.count(i)
        counts[i]=count   
    t2=sorted(counts.items(), key=lambda item:item[1], reverse=True)      #按字符出现次数的大小排列
    print(t2)
def main(text):              #定义一个主函数，后续直接调用它就行了
    stats_text_en(text)       #把统计英文的函数放进来，作为它的子函数
    stats_text_cn(text)       #把统计中文的函数也放进来，作为它的子函数
main(t)                       #调用主函数