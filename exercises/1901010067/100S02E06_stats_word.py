text = '''
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
Python是一种计算机程序设计语言。是一种动态的、面向对象的脚本语言，最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，越来越多被用于独立的、大型项目的开发。
'''
def stats_text_en(text):#处理英文文本，按单词出现次数，降序排列
    text=text.replace('.',' ').replace(',',' ').replace('!',' ').replace('--',' ').replace('*',' ')#把非英文字符替换为空格
    text=text.lower()#把所有单词变为小写
    text=text.split()#以空格拆分为独立单词
    dic={}
    for i in text:  #将字符串转换为字典
        count=text.count(i)
        r1={i:count}
        dic.update(r1)
        #print(i,'',count )
    print(dic)
    print(end='\n')
    print("按出现次数从大到小排列")
    dic1=sorted(dic.items(),key=lambda x:x[1],reverse=True) #按照单词出现次数，从大到小排序
    print(dic1)

stats_text_en(text)


text= """
自学的过程，实际上需要拆解为以下四个阶段，虽然它们之间常常有部分重叠：
学
练
用
造
只要识字，就会忍不住阅读；只要感觉上有“值得学”的，就会忍不住去学 —— 事实上每个人时时刻刻都在学习，只不过，学习的目标选择与学习的方式以及效率均不相同而已。
绝大多数人从未区分过这些个阶段，也从未研究过这几个阶段分别应该如何对待。这就解释了为什么那么多人虽然总是忍不住阅读，总是忍不住学习，
但，终其一生都没有真正掌握过像样的技能…… 因为他们在第一个阶段就出错，到了第二个阶段就放弃，第三个阶段是直接跳进去的，总是“对付着用”，
至于第四个阶段么，想都没想过……
第一部分的内容，基本用来展示“学”的过程。学，就需要重复，甚至很多次重复，尤其是在面对充满了“过早引用”现象的知识结构的时候。
反复学，最锻炼的是“归纳整理”的能力。而且，最有意思的，这在大多数情况下还是自动发生的 —— 只要你不断重复，你的大脑会在不自主
之间把那些已经掌握的知识点与当前尚未掌握的知识点区分开来，前者处理起来轻松容易，甚至可以跳过；后者需要投入更多的注意力去仔细处理…… 在这个过程中，
绝大多数的归纳整理工作自动完成了。最后再加上一点“刻意的、收尾性的归纳总结整理工作” —— 大功告成。
"""

cndic={}                    #初始化一个空的字典
def stats_text_cn(text):    #定义检索中文函数
    for i in text:
        if u'\u4e00' <= i <= u'\u9fff':#判断是不是中文
            cndic[i] = text.count(i)
    return cndic
stats_text_cn(text)
cndic=sorted(cndic.items(),key=lambda item:item[1],reverse = True) 
print(cndic)
