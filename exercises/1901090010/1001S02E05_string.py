
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

text.replace("better","worse")
new_text = text.replace("better","worse")
print(new_text)
# 1.替换掉所有的符号
word_str = new_text.replace(',','').replace('.','').replace('!','').replace('*','').replace('--','')
# 2.按照空格将所有的单词分割开
word_list = word_str.split()
word_list = word_str.split()
y = []
for word in word_list:
    # 查找不包含ea的单词
    if word.find('ea') < 0:
        y.append(word)
new_text2 = ' '.join(y)
print(new_text2)
new_text3 = new_text2.swapcase()
print(new_text3)
new_text4 = new_text3.split()
new_text4.sort()
print (new_text4)

