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
#这段我想用正则表达式试试的，但是挑出带“ea”的字符后，下一步不会了
#text_1 = text.replace("better", "worse")
#text_2 = text_1.split() #把字符串转变成列表
#text_3 = re.compile(r'.ea.') #使用前需import re
#text_4 = text_3.findall(text) 

text_1 = text.replace("better", "worse") #第一步
text_2 = text_1.split()
text_3 = []

#另一种解决方法
#for text_1 in text_2:
#    if text_1.find("ea") < 0:
#        text_3.append(i)
#print(text_3)

for text_1 in text_2:
    if "ea" not in text_1:
        text_3.append(text_1)
#print(text_3) # 第二步

text_4 = " ".join(text_3)
text_5 = text_4.swapcase().replace(",", "").replace(".", "").replace("-", "").replace("!", "").replace("*", "") #第三步
print(sorted(text_5.split(), key=str.lower)) #第4步
#总结：做作业的过程中，就像吃百家饭一样，参考借鉴比较多。
#什么时候能一口气流畅的独立的写出代码啊！！！