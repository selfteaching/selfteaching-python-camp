

def stats_text_en(a):#创造函数
    b = a.split(" ")#分割text
    c = { }
    for i in b:
        count = b.count(i)
        r1={i:count}#计算出现频率
        c.update(r1)#更新计算频率
    c1=sorted(c.items(),key=lambda x:x[1],reverse=True)#升序排序
    print(c1)#打印
   

text = '''The Zen of Python, by Tim Peters
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
Namespaces are one honking great idea -- let's do more of those!'''
stats_text_en(text)


def stats_text_cn(text):#设定函数
    A= []
    for i in text:
        i.strip( '",",，,！,。,? ,“,—' )
        A.append(i)#转变形式
        for x in A:
            count=A.count(x) 
            d={x:count}#计算出现次数
            c.update(d)#更新出现次数
    c1=sorted(c.items(),key=lambda x:x[1],reverse=True)#降序排列
    print(c1)
e = '''细想想，每个人都有很多很多“積ん読”。小时候我们拿回家的教科书中就有相当一部分，其实就是“積ん読”，虽然那时候掏钱买书的是父母，不仔细看、或者干脆不看的时候，也知道自己在偷懒…… 再后来就是“主动犯罪”了 —— 比如，很多人买到手里的英语词汇书是根本就没有翻到过第二个列表的，乃至于过去我常常开玩笑说，中国学生都认识一个单词，abandon，不是吗？这个单词是很多很多人“决心重新做人”而后“就这样罢”的铁板钉钉的见证者。'''
stats_text_cn(e)