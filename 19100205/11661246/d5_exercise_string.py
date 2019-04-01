str = '''
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
str=str.replace( 'better', ' worse' ) #替换
print (str)

# 删除包含ea的单词
list_str = str.split () # 将字符串转换为列表
list_str1 = [] 
for i in list_str:
    if 'ea' not in i:
        list_str1.append(i) # 此循环用if条件删除包含ea的单词
str = " ".join(list_str1) #将列表转换为字符串
print(str)

# 大小写翻转
str = str.swapcase()
print(str)

# 单词按升序排列
str = str.replace('.', '')
str = str.replace('!', '')
str = str.replace('--', '')
str = str.replace('*', '')
str = str.replace(',', '') # 去除标点符号
list_str1 = str.split ()
list_str1.sort() # 列表中的元素（单词）进行排序
print(list_str1)

