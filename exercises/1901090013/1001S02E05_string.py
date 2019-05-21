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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

# 将字符串样本text里的更好全部替换成更糟
# 注意字符串是不可变对象，我们替换之后，需要用变量接收一下新的字符串
# 一开始用ctrl+H完成。。。
new_text = text.replace('better','worse')
print(new_text)

# 将单词中包含ea的单词剔除（这一步实在不会做。。。）
# 1.替换掉所有的符号
word_str = new_text.replace(',','').replace('.','').replace('!','').replace('*','').replace('--','')
# 2.按照空格将所有的单词分割开
word_list = word_str.split()
y = []
for word in word_list:
    # 查找不包含ea的单词
    if word.find('ea') < 1:
        y.append(word)
new_text2 = ' '.join(y)
print(word_list)

# 将上一步的结果里的字母进行大小写翻转（将大写字母转成小写，小写字母转成大写）

#------------只通过小写和大写方法实现-----------
# low = new_text2.lower()
# new_text3 = ''
# for word in new_text2:
#     if word in low:
#         new_text3 += word.upper()
#     else:
#         new_text3 += word.lower()
# print(new_text3)
#------------简便方法实现-----------
new_text3 = new_text2.swapcase()
print(new_text3)

# 将上一步的结果里所有单词按a ... z升序排列，并输出结果
new_text4 = new_text3.split()
new_text4.sort()
print(new_text4)