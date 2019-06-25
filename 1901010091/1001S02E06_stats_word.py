print('英文词频统计排序函数测试结果')
text1='''
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
'''

def stats_text_en(text):
    t1=text.split()#将字符串转化为列表
    word=[]
    s=',.*-!'#去除非英文字符
    for i in t1:
        for j in s:
            i=i.replace(j,'')
        if len(i):
            word.append(i)
    #统计词频
    counter={}
    w1=set(word)
    w2=list(w1)
    for a in range(len(w2)):
        counter[w2[a]]=0
        for b in range(len(word)):
            if w2[a]==word[b]:
                counter[w2[a]]+=1
    #词频排序
    result=sorted(counter.items(),key=lambda item:item[1],reverse=True)#items()函数将字典转化为元组，key lambda item：item[1]表示选第二个元素做比较，reverse表示降序
    print(result)

stats_text_en(text1)

print('中文字频统计排序函数测试结果')
def stats_text_en(text):
    word_lst=[]
    word_dict={}
    
    exclude_str="，。！？、（）【】《》,.<>=：+-*——“”...1234567890"
    
    textin=text.split()
    textout=[]
    #添加每一个字到列表中
    for line in textin:
        for char in line:
            word_lst.append(char)

    #用字典统计每个字出现的次数
    for char in word_lst:
        if char not in exclude_str:
            if char.strip() not in word_dict:#去除各种空白
                word_dict[char]=1
            else:
                word_dict[char]+=1

    #按字频排序
    textout=sorted(word_dict.items(),key=lambda x:x[1],reverse=True)

    #输出结果
    print('字符\t字频')
    print('============')
    for e in textout:
        print('%s\t%d'%e)
    

text1='''巴菲特：当我们收购的时候，是800亿-900亿，1000亿甚至是2000亿美元，都不会有太多的差别。我们怎么做股票回购的策略上不会有大的改变。'''

stats_text_en(text1)