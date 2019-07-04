en_text = '''
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
cn_text = '''城市群形成和发展的本质过程和直观表
现是城市群体结构或城市群形态结构产生、发展到成
熟完善的过程。文章从城市群体结构的概念入手, 研
究了其基本型式和结构划分的思路, 概括了四圈层空
间结构模式, 即核心首位城市带、城市组群发育带、
城市个体分布带、城市群腹地带。分析了其结节性与
均质性、网络性、功能性的特征, 并对城市群体结构
发展动力、阶段及特征加以理论概括。以城市群演化
为基点, 对城市群体形态结构、类型和演化规律予以
阐述, 归纳出城市群体结构和城市群形态类型演化的
相关模式。'''

import re

def stats_text_en(text):
    ''' count the number of every English word in a text '''
    text = text.lower()
    import re
    text_list = re.findall(r'\w+', text)
    text_set = set(text_list)
    d = {x:text_list.count(x) for x in text_set}
    d_list = [v for v in d.values()]
    d_list.sort(reverse=True)
    return d_list

stats_text_en(en_text)


def stats_text_cn(text):
    ''' count the number of every Chinese character in
    a text '''
    import re
    text_list = re.findall(r'([\u4e00-\u9fff])',text)
    text_set = set(text_list)
    d = {x:text_list.count(x) for x in text_set}
    d_list = [v for v in d.values()]
    d_list.sort(reverse=True)
    return d_list

stats_text_cn(cn_text)
