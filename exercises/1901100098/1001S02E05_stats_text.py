# 统计字符串中英文单词出现的次数
sample_text='''
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
elements=sample_text.split()
words=[]
#先根据列表选出需要剔除的非单词符号
symbols=',.*-!'
for element in elements:
#遍历一遍要剔除的符号
    for symbol in symbols:
 #逐个替换字符号，用''替换字符所占位置      
        element=element.replace(symbol,'')
#剔除后，如果element的长度不为0则是正常单词
    if len(element):
       words.append(element)
print('正常的英文单词==>',words)

#初始化一个 dict （字典）类型的变量，用来存放单词的次数

counter = {}
# set(集合类型) 可以去掉列表里的重复元素，可以在for...in里减少循环次数
word_set = set (words) 
for word in word_set:
        counter[word]=words.count(word)
print('英文单词出现次数==>',counter)

# 2.按照单词出现次数从大到小输出所有单词及出现次数
# 内置函数 sorted 的参数key 表示按照函数的那一项值进行排序
# dict 类型的counter的 items方法 会返回一个包含相应项（key,value）的元组列表  （本实例中key代表单词，value 代表次数）
print('从大到小暑促所有单词及出现次数==>',sorted(counter.items(),key=lambda x :x[1],reverse=True))
