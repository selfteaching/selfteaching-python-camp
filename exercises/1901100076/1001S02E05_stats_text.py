text1= """The Zen of Python, by Tim Peters
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
  """
text2= text1.split()

#define new quantity to save new list without symbol 
text3=[]

symbols="*,.-!"
for word in text2:

   for symbol in symbols:
     word=word.replace(symbol,"")#剔除符号

   if len(word):#判断单词的长度
       text3.append(word)

#print(text3)
     
text4 ={} #初始化字典变量
de_word=set(text3)# 消除重复元素
for word in de_word: #每个单词的次数
   text4[word] =text3.count(word)
   
print(text4)

print("",sorted(text4.items(),key=lambda x:x[1],reverse=True))#Lambda 表达式¶


"""
为什么不能这么样直接用呢
for a, b in zip(single_word,word_count):
    print("{0}:{1}" .format(a,b))
"""



