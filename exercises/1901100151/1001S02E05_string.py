# from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = "all"

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
'''

print()
print("使⽤用字典dict统计字符串样本text中各个英⽂单词出现的次数:\n")

# text1 = []
# text1 = list(text)
# print(text1)

# error:
# text2 = split(text)
# right:
# text2 = text.split()
# print(text2)

# 分割字符串
a = text.split()
print(a)
# 设置存贮单词的列表
b = []
c = ".,!*-"
for d in a:
    # 需要去除的标点字符
    for e in c:
        d = d.replace(e,"")
        # print(d)
    # 为b列表存储单词
    if len(d):
        b.append(d)
print("统计单词:\n",b)

# 设置字典
f = {}  
h = set(b)  
for g in h:
    f[g] = b.count(g)
print("英文单词出现次数:\n",f)
print("英文单词出现次数从大到小顺序:\n",sorted(f.items(),key = lambda x: x[1], reverse = True))
# print("英文单词出现次数从大到小顺序:\n",sorted(f))