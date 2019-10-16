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

#从上一步的结果，将单词中包含 ea 的单词剔除
    #先以‘’为分割单位，把字符串转化为单词数组
result = text.split()  
symple_set = ".,*-!"
word_list = []
for item in result:
    
    # 排除单词中的特殊字符
    for symple in symple_set:
        item = item.replace(symple,'')  # 这儿犯了一个错， .运算，也就是一个对象的方法不会改变这个对象本身，而是会返回另外一个对象
    #排除含有”ea“ 的单词
    if "ea" not in str(item) and item != '':
        word_list.append(item)
# print(word_list)        
# 将上一的结果⾥的字母进⾏大小写翻转(将大写字⺟转成⼩写，⼩写字母转成大写) 
for index in range(len(word_list)):
    word_list[index] = str(word_list[index]).swapcase() #这个函数是自己之前并知道，其实遍历是常用的方法
# print(word_list)            
# 将第上异步的结果里所有单词按a...z升序排列，并输出结果) 
print(sorted(word_list,reverse = False))
