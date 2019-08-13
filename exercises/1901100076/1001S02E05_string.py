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

text2=text1.replace("better","worse")
#print(text2)
#将单词中包含 ea 的单词剔除
text3=text2.split()
#text4=[]
"""
for word in text3:
     if word.find("ea")<0:
       text4.append(word)
 
print(text4)
"""
for word in text3:
     if word.find("ea")>0:
         text3.remove(word)

#print(text3)
"""
字符串合并在一起
text4="\t".join(text3)

print(text4)
"""
text4=[i.swapcase() for i in text3]
#print(text4)

text5=sorted(text4,reverse=True)
print (text5)





    
