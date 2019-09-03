en_text='''
The Zen of Python,by Tim Peters


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
In the face of ambxiquity,refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Altough that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain,it's a bad idea.
If the implementation is easy to explain,it's a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
 #英文降序
def stats_text_en (text):
    eles=text.split()#将文章按照空格划分开
    words=[]
    sys=".,-,*,!"
    for elet in eles:
        for s1 in sys:
            elet=elet.replace(s1,' ')
        if len(elet) and elet.isascii():
            words.append(elet)
    print(words)
    print()

    counter={}
    word_set=set(words)
    for word in word_set:
        counter[word]=words.count(word)
    print(counter)
    print()

    return sorted(counter.items(),key=lambda x:x[1],reverse=True)

#中文降序
def stats_text_cn (text):
    cn_characters=[]
   
    for character in text:
        
        if '\u4e00'<=character<='\u9fa5':#中文范围
            cn_characters.append(character)

    counter={}
    cn_set=set(cn_characters)
    for word in cn_set:
        counter[word]=cn_characters.count(word)

    return sorted(counter.items(),key=lambda x:x[1],reverse=True)


cn_text='''
Python之禅 by Tim Petters

美丽胜于丑陋
露骨比露骨好
简单总比复杂好
复杂比复杂好
平的比嵌套的好
稀疏比密密好
可读性很重要
特殊情况并不足以打破规则
尽管实用性胜过纯洁性
错误永远不应该悄悄过去
除非明确地沉默
面对橱柜，拒绝诱惑去猜测
应该有一种----最好只有一种----显而易见的方法来做到这一点
如果你不是荷兰人，那么这种方式在一开始可能并不明显
现在总比没有好
虽然从来没有比现在更好
如果实现很难解释，这是一个坏主意
如果实现容易解释，这是一个好主意
命名空间是一个很好的主意--让我们做更多的那些
'''

#输出合并词频统计结果
def stats_text(text):
    return stats_text_en(text) + stats_text_cn(text)
#def stats_text(en_text,cn_text):
    #print("输出合并词频统计结果\n",stats_text_en(en_text) + stats_text_cn(cn_text)) 

if __name__=='__main__':
    
    en_result=stats_text_en(en_text)
    cn_result=stats_text_cn(cn_text)
    print("统计英文次数-->\n",en_result)
    print("统计中文次数-->\n",cn_result)



   


