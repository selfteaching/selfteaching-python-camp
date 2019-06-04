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
text = text.replace('better', 'worse') # 用worse替换better
print(text)

# 删除包含ea的单词
list_text = text.split () # 将字符串转换为列表
list_text1 = []
for i in list_text:
    if 'ea' not in i:
        list_text1.append(i) # 此循环用if条件删除包含ea的单词
text = " ".join(list_text1) #将列表转换为字符串
print(text)
print("")
# 大小写翻转
text = text.swapcase()
print(text)
print("")
# 单词按升序排列
text = text.replace('.', '')
text = text.replace('!', '')
text = text.replace('--', '')
text = text.replace('*', '')
text = text.replace(',', '') # 去除标点符号
list_text1 = text.split ()
list_text1.sort() # 列表中的元素（单词）进行排序
print(list_text1)
