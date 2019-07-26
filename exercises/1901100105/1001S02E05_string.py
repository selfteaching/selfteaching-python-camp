sample_text = '''
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
Namespaces are on honking great idea -- let's do more of those!
'''

#对象.方法(参数)

# 1. 将字符串样本里的 better 全部换成 worse
text = sample_text.replace('better', 'worse')
print('将字符串样本里的 better 全部替换成 worse ==>', text)

# 2. 将单词中包含ea的单词剔除
words = text.split() #通过空格对字符串进行切片
filtered = [] #用一个列表类型的变量存放过滤完的单词
for word in words: #进入循环语句
    if word.find('ea') < 0:
        filtered.append(word) #添加
print('将单词中包含ea的单词剔除 ==>', filtered)

# 3. 大小写翻转，大写转小写，小写转大写
swapcased = [i.swapcase() for i in filtered] 
# 尝试修改语句成 filtereddd = str(filtered)
# swapcased = filtereddd.swapcase(), 运行成功，但因将文本分割成了字母，导致继续运行第4结果有误。须用split分隔再排序
print('进行大小写反转 ==>', swapcased)

#4.所有单词按a...z升序排列，并输出
print('单词按从a到z升序排列 ==>', sorted(swapcased)) #尝试修改，swapcaseed = swapcased.split()，运行成功
# print('降序排列', sorted(swapcased, reverse=true))

