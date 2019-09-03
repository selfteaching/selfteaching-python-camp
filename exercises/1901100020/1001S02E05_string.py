# 1. 替换
# 定义text这个字符串
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
# 定义完毕
# text.replace("better","worse"): 其中的text为前面定义的操作对象，replace为函数
# print为输出
print("将字符串串样本 text⾥的better全部替换成worse后的文本如下：")
print(text.replace("better","worse"))


# 2.提出包含ea的单词
# 先将字符串根据“空白字符”分割成list，要调用str类型
words = text.split()
# 定义1个list类型的变量用来存放过滤完的单词
filtered = []
# 用for…in循环遍历一遍words里元素然后判断单词是否包含"ea"
for word in words:
    # str类型的find方法，如果不包含“参数”则返回“-1”，如果包含则返回该字符第一次出现时的索引
    if word.find('ea')<0:
        filtered.append(word)
print('将单词中包含ea的单词剔除掉 ==>',filtered)

# 3.对大小写进行翻转
# 利用列表推导式对str类型的元素进行大小写翻转
swapcased = [i.swapcase()for i in filtered]
print("将大小写翻转 ==>",swapcased)

# 4.单词按a到z升序排列
print('单词按a到z升序排列 ==>',sorted(swapcased))



