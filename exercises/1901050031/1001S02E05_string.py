sample_text='''
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

# 1.将字符串样本里的better全部替换成worse
 
#调用str类型的replace方法进行替换
text= sample_text.replace('better','worse')
print('将字符串样本的better全部替换成worse==>',text)

# 2.将单词中包含ea的单词剔除
 
#先将字符串根据 空白字符 分割线 list ，要调用str类型
words=text.split()
#定义一个 list 类型的变量用来存放过滤完的单词
filtered=[]
# 用for...in循环遍历一遍 words里面元素然后判断单词是否包含ea
for word in words:
    #str类型的find方法 如果不包含 参数 字符则返回-1，如果包含则返回该字符第一次出现时的索引
    if word.find('ea')<0:
        filtered.append(word)
print ("将单词中包含ea的单词剔除==>",filtered)

#3.进行大小写翻转
#利用列表推倒式 对 str 类型的元素进行大小写翻转
swapcased=[i.swapcase()for i in filtered]
print('进行大小写翻转==>',swapcased)

#4.单词按a...z升序排列
print('单词按a...z升序排列==>',sorted(swapcased))
#print(单词按a...z降序排列)==>',sorted(swapcased,reverse=Ture)



