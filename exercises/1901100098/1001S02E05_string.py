simple_text='''
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
#1.将字符串样本 text ?的 better 全部替换成 worse

# 调用str类型的 replace 
text=simple_text.replace('better','worse')
print('将字符串样本 text ?的 better 全部替换成 worse ',text)
# 2.将单词中包含 ea 的单词剔除
# 先将字符串根据 空白字符 分割成list ,要调用str类型 split
words=text.split()
# 定义一个list 变量来存放 过滤后的单词要调用list类型的 filter
filtered=[]
# 用 for...in  循环一遍words 里的元素，然后判断单词里的元素是否包含ea
for word in words:
    if word.find('ea')<0:
        filtered.append(word)
print('将单词中包含 ea 的单词剔除',filtered)

# 3 进行大小写反转
swapcased=[i.swapcase() for i in filtered]
print('大小写反转',swapcased)

#5、单词按照A到Z升序排序
print('单词按照升序排列',sorted(swapcased))

