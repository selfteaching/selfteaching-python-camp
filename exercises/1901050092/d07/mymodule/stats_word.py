def  stats_text_en(text):
    '''封装统计英文单词词频的函数'''
    elements=text.split()
    words=[]
    symbols=' ,.*-!'
    for element in elements:
        for symbol in symbols:
            element=element.replace(symbol,'')
        if len(element)and element.isascii():
            words.append(element)
    counter={}
    word_set=set(words)
    for word in word_set:
        counter[word]=words.count(word)
    return sorted(counter.items(),key=lambda x: x[1],reverse=True)



def  stats_text_cn(text):
    '''封装统计中文汉字字频的函数'''
    cn_charaters=[]
    symbols=', .*-!， '
    for charater in text:
        for symbol in symbols:
            charater=charater.replace(symbol,'')
        if '\u4e00 <=charater <=u9fff':
            cn_charaters.append(charater)
    counter={}
    cn_charater_set=set(cn_charaters)
    for charater in cn_charater_set:
        counter[charater]=cn_charaters.count(charater)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)

def stats_text(text):
    '''
    合并中，英文词频的结果
    '''
    return stats_text_en(text) + stats_text_cn(text)


en_text='''
The Zen of Python,by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren`t special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity,refuse the temptation tu guess.
There should be one--and preferably only one--obvious way to do it.
Although that way may not be obvious at fitst unless you`re Dutch.
Now is better than never.
Although never is often bettet than*right*now.
If zhe implementation is hard to explan,it`s a bad idea.
If zhe implementation is easy to explan,it may be a good idea.
Namesoaces are one honking great idea--let`s do more of those!
'''
cn_text='''
只要识字，就会忍不住阅读；只要感觉上有“值得学”的，就会忍不住去学——事实上每个人时时刻刻都在学习，只不过，学习的目标选择与学习的方式以及效率均不相同而已。
绝大多数人从未区分过这几个阶段，也从未研究过这几个阶段分别应该如何对待。这就解释了为什么那么多人虽然总是忍不住阅读，总是忍不住学习，但终其一生都没有真正掌握过像样的技能…… 
因为他们在第一个阶段就出错，到了第二个阶段就放弃，第三个阶段是直接跳进去的，总是 “对付着用”，至于第四个阶段么，想都没想过……
第一部分的内容，基本用来展示 “学” 的过程。学，就需要重复，甚至很多次重复，尤其是在面对充满了 “过早引用” 现象的知识结构的时候。
反复学，最锻炼的是 “归纳整理” 的能力。
而且，最有意思的，这在大多数情况下还是自动发生的 —— 只要你不断重复，你的大脑会在不自主之间把那些已经掌握的知识点与当前尚未掌握的知识点区分开来，前者处理起来轻松容易，甚至可以跳过；
后者需要投入更多的注意力去仔细处理…… 在这个过程中，绝大多数的归纳整理工作自动完成了。最后再加上一点 “刻意的、收尾性的归纳总结整理工作” —— 大功告成。
'''


if __name__ =='__main__':
    en_result= stats_text_en(en_text)
    cn_result= stats_text_cn(cn_text)
    print('英文单词出现次数\n',en_result)
    print('中文出现次数\n',cn_result)