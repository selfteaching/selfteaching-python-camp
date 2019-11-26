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
# 使用字典(dict)统计字符串样本中各个英文单词出现的次数

# 先将字符串根据 空白字符 分隔成 list，要调用 str 类型
elements = text.split()

# 定义一个新的 list 型变量，储存处理过的单词
words = []

# 先针对样本文本挑选出要剔除的非单词符号
symbols = ',.*-!'

for element in elements:   # 遍历一遍要剔除的符号
    for symbol in symbols:  # 逐个替换字符号
        element = element.replace(symbol,'') #将元素中的符号去除，同时用''删除符号所占位置
    if len(element): # 剔除类字符后如果 element 的长度不为0，则算作正常单词
        words.append(element)     #将非单词的空白，符号等去除，append()本身就是可变序列
print('除去空白和符号的单词 ====>\n',words)  #如果print在if下，就会打印非常多行，此处应该在第一个for之下

#容器数据类型,是一个dict子类，初始化一个 dict（字典）类型的变量，用来存放单词出现的次数
counter = {}  
word_set = set(words)  #set是内置类型，可返回一个新的对象，去掉 列表 里的重复元素
for word in word_set:
    counter[word] = words.count(word) 
print('英文单词出现的次数 ====>\n',counter)  #输出为无序

# 2.按照出现次数从大到小输出所有的单词及出现的次数 (之前忘记做这一步了)

# 内置函数 sorted 的参数 key 表示按元素的那一项的值进行排序
# dict 类型 counter 的 items 方法会返回一个 包含 相应 项（key,value) 的 元组 列表
# print('counter.items()==>',counter.items())
print('从大到小输出所有的单词及出现的次数 ====>',sorted(counter.items(),key = lambda x:x[1],reverse = True))