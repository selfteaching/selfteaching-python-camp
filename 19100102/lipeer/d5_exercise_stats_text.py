s = "Count, the number of spaces."
print s.count(" ")
x = "I like to program in Python"
print x.count("i")


import collections
import re
 

句子 = "This is a sentence"    #可以写别的
 
字典 = {}
 
句子拆成的单词列表 = 句子.split()
 
for 单词 in 句子拆成的单词列表:
    if 单词 in 字典.keys():
        字典[单词] += 1
    else:
        字典[单词] = 0
 
for 单词,次数 in 字典.items():
    print('%-20s:'%单词,次数)


import re
print re.sub('[^a-zA-Z]','',oldS)
