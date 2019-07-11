<<<<<<< HEAD
sample_text =
text = sample_text.replace('better','worse')
print('将字符串样本里的 better 全部替换成 worse ==>', text)
words = text.split()
filtered = []
for word in words:
    if word.find('ea') < 0:
        filtered.append(word)
print('将单词中包含 ea 的单词剔除 ==》'，filtered)
swapcased = [i.swapcased() for i in filtered]
print('进行大小翻转 ==》'，swapcased)
print('单词按 a...z 升序排列 ==》'，sorted(swapcased))
=======
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
new_text=text.lower().replace('better','worse') #定义一个新的文本new_text区别于旧文本，然后用str.replace()替换
print(new_text) #显示新文本
words = new_text.split() #把text文本进行拆分，变成list
new_list = [] #建立一个空白的列表，准备把去掉ea的字符放入
for word in words: 
    if word.find('ea')< 0: #用查找，如果没有找到为返回值为-1，即不包含ea的字符
        new_list.append(word)  #把这些字符放入new_list（特别注意：一定要注意冒号是否是英文的，还要特别注意缩进的格数，缩进4格）
        
print('打印剔除ea之后的单词:',new_list)   #打印验证结果
new_text2 = ''.join(new_list)  #把列表转化为字符串
new_text3 = new_text2.swapcase()  #定义新的字符串，用swapcase()把大小写字母逐个翻转
print(new_text3)  #显示验证结果
new_text4 = new_text3.split()  #把text4 重新变成列表
new_text4.sort()  #用sort()为列表排序
print(new_text4) #显示验证结果
>>>>>>> 79aea0d0277b4207978227c514aa768686cb7878
