text ='''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
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
#第一步 将字符串样本text⾥里里的better全部替换成worse
text = text.replace("better","worse")

result = text.split()
# print(text) 
#从第上一步的结果里，将单词中包含 ea 的单词剔除
word_list = []
for item in result:
    if item.find("ea") < 0:
        word_list.append(item)
# print(word_list) 
# 将上一步的结果里的字⺟进⾏⼤小写翻转
result = [word.swapcase() for word in word_list]
# print(result)
# 将第上一步的结果里面所有单词按a...z升序排列列，并输出结果
print(sorted(result))