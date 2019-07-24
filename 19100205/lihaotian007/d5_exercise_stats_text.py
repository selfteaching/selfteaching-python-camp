string_a = '''\
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
Unless explicitly silenced. In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch. Now is better than never.
Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!
'''
list_c = []
list_d = []
list_e = []
i = 0
j = 0
#将字符串string_a，封装入列表
for i in range(len(string_a)) :
    if (string_a[i] == ' ') or (string_a[i] == '.') or (string_a[i] == ',') or (string_a[i] == '-') or (string_a[i] == '*') or (string_a[i] == '!') or (string_a[i] == '\n') :
        if i == j :
            j = i+1
        else :
            list_c.append(string_a[j:i])
            j = i+1
print('封装后的TexT：',list_c,end='\n\n')
# 用字典统计词频
dic_f = {}
for i in range(len(list_c)) :
    if list_c[i] not in dic_f :
        dic_f[list_c[i]] = 1
    else :
        dic_f[list_c[i]] = dic_f[list_c[i]] + 1
print(dic_f)
# 按词频排序
print(sorted(dic_f.items(),key = lambda x:x[1],reverse = True))