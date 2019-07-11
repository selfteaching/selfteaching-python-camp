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
result = text.split()  
symple_set = ".,*-!"
word_list = {}
for item in result:    
    # 排除单词中的特殊字符
    for symple in symple_set:
        item = item.replace(symple,'')  
    #排除含有”ea“ 的单词
    if item in word_list.keys():
         word_list[item] += 1
    elif item.isalpha():#统计非字母单词出现的频率
         word_list[item] = 1 

# 按照出现次数从⼤大到⼩小输出所有的单词及出现的次数
     # 关键在于对word_list.items()的理解，以及lambda的理解
print(sorted(word_list.items(),key = lambda x:x[1],reverse = True))
