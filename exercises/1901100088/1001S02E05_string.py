#1. 创建⼀一个名为  的文件
text='''
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
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

print("2. 将字符串串样本text⾥里里的better全部替换成worse")
string_2 = text.replace("better","worse")
print(string_2)
print()


print("3. 从第 2 步的结里，将单词中包含 ea 的单词剔除")
print("解法一")
words = string_2.split()
print(words)
text_3 = []
for word in words:
    if "ea" not in word:
        text_3.append(word)
string_3 = " ".join(text_3)
print(string_3)
print()

print("3. 解法二")
words_2 = text.split()
for word_2 in words_2:
    if "ea" in word_2:
        words_2.remove(word_2)
string_3_2 = " ".join(words_2)
print(string_3_2)
print()


print("4. 将第3步的结果的字⺟进行大小写翻转(将⼤写字母转成小写，⼩写字⺟转成⼤写)")
string_4 = string_3.swapcase()
print(string_4)
print()

print("5. 将第4步的结果⾥所有单词按a...z升序排列，并输出结果")
test_1 = string_4.split(" ")
string_5 = " ".join(sorted(test_1))
print(string_5)