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

#将字符串‘better’替换为‘worse’
for i in range(len(list_c)) :
    if list_c[i] == 'better' :
        list_c[i] = 'worse'
print('替换后的TexT：',list_c,end='\n\n')

#将含有‘ea’的字符串删掉
j = 0
list_d = []
for i in range(len(list_c)) :
    if 'ea' not in list_c[i] :
        list_d.append(list_c[i])
        j += 1
print('删除后的TexT：',list_d,end='\n\n')

list_e = []
#将大小写翻转
for i in range(len(list_d)) :
        for j in range(len(list_d[i])) : #将列表中的字符串分别进行转换
                if ord(list_d[i][j]) in range(65,91) :
                        list_e.append(chr(ord(list_d[i][j])+32))
                elif ord(list_d[i][j]) in range(97,123) :
                        list_e.append(chr(ord(list_d[i][j])-32))
        list_d[i] = ''.join(list_e[0:j+1]) #将分别转换后的字符串重新放回list_d中
        list_e.clear() #对过程数据清洗
print('转换后的TexT：',list_d,end='\n\n')