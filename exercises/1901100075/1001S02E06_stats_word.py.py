#1. 封装统计英⽂单词词频的函数
def stats_text_en(text):
#将str类型切割成list类型    
    elements=text.split()
    b=[]
    a=',.*!-'
    for element in elements:
        for aa in a:
            element=element.replace(aa,'')
        if len(element):
            b.append(element)
    counter={}
    b_set=set(b)
    for c in b_set:
        counter[c]=b.count(c)
    #函数返回值用return进行返回，   如果没有return返回值则为none
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)

#统计中⽂汉字字频的函数
def stats_text_cn(text):
    text=text.replace(',','').replace('；','').replace('！','').replace('\n','').replace('，','')
    d={}  
    for e in text:
        d.update({e:text.count(e)}) 
    print(d)    
    f=sorted(d.items(),key=lambda x: x[1],reverse=True)
    print(f)
text1 = '''
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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
text2='''
忽然，很想醉，是因为早已心碎；
忽然，很想睡，是因为心里早已疲惫，
忽然，很想喝一杯咖啡，是因为要映衬内心的苦味；
忽然，很想一个人颓废，是因为再没有什么人让我不累!
我把你嵌在一滴泪里.幻想千年后的琥珀,我不敢低头,怕那滴泪坠下,碎了你,碎了我.碎了千年的梦,若有来生必踏遍千山万水寻找你
我像一朵孤云
'''
if __name__ == '__main__':
    text1=stats_text_en(text1)
    print(text1)
    stats_text_cn(text2)