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

def stats_text_en(t):
    t1 = t.lower()
    t_list = t1.split()
    dict1 = {}
    for i in t_list:
        ii = i.strip(' ,.*!-')
        if ii not in dict1:
            dict1[ii] = 1
        else:
            dict1[ii] = dict1[ii] + 1
    dict2 = sorted(dict1.items(),key = lambda x:x[1],reverse = True)
    return dict2
print('text1:')
print(stats_text_en(text1))
print('\n')



text2 = '''
/“/请/！/”/“/请/！/”/两名/剑士/各自/倒转/剑尖/，/右手/握/剑柄/，
/左手/搭于/右手/手背/，/躬身行礼/。/两/人/身子/尚未/站/直/，
/突然/间/白光闪/动/，/跟着/铮的/一/声响/，
/双剑相/交/，/两/人/各/退一步/。
/旁/观众/人/都/是/“/咦/”/的/一声/轻呼/。/青衣/剑士/连/劈/三/剑/
'''

text3 = '''
二 结构化思维，几乎是最值得刻意训练的能力！
然而在现实中，很多人往往忽略结构化思维的培养，因为他们认为，这是天生的。他们要么觉得自己足够聪明所以不需要培养，要么觉得我天生不聪明，学不来，干脆放弃。
我曾经在文章中提到过能力的重要性。有人问，能力有那么多，到底培养哪一个才好呢？如果我用一个两维矩阵来分析的话，可以看到，结构化思维能力，是既能够被培养同时价值度又高的能力。
'''

def stats_text_cn(t):
    t_list = []
    t_dict = {}
    exclude_str = '\n ，。！？/”“'
    for char in t:
        t_list.append(char)
    for char in t_list:
        if char not in exclude_str:
            if char.strip() not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] = t_dict[char] + 1
    t_dict2 = sorted(t_dict.items(),key = lambda x:x[1],reverse = True)
    return t_dict2
print('text2:')
print(stats_text_cn(text2))
print('\n')
print('text3:')
print(stats_text_cn(text3))