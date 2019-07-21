sample_text = ''' 
The Zen of Python, by Tim Peters


Beautiful is better than ugly. 
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 
Flat is better than nested. 
Sparse is better than dense.
Readability counts
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

#1.将字符串样本里的better 全部替换成worse
text= sample_text.replace('better','worse')
print(' 将字符串样本 text ⾥的 better 全部替换成 worse:',text)

#2. 将单词中包含ea的单词删除
#自己搞了好久没有搞定，还是参照教练给的视频
# 感觉应该有更容易的方法把。
# 查了字符串的method,没有简单查找删除的办法。
#自己的想法如下：##########################
#找查找的method，把含有ea的单词找出来，
# 但是要用到循环，一直查找，接着删除
###############################################
# 先将字符串根据空白字符分割成list,要调用str类型
#？这里不太能理解为什么要分割成list#
words=text.split()
filtered=[]
for word in words:
    if word.find('ea') <0:
        filtered.append(word)
print ('将单词中包含ea的单词剔除',filtered)

#3. 进行大小写翻转
swapcased=[i.swapcase()for i in filtered]
print('进行大小写翻转',swapcased)

#4.单词按a...z 升序排列
print('单词按a...z 升序排列', sorted(swapcased))


