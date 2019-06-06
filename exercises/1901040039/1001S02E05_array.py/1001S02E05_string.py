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
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
# 1.把 better 替换成 worse
print('better' in text)
text.replace("better","worse")
print(text.replace("better","worse"))
#将包含ea的单词去除
split_text=text.split()
print(split_text)
except_text=""
for words in split_text:
          if"ea"in words:
                 continue
          else:
                  except_text = except_text + " " + words
print(except_text)                  
#将所有字母大小写翻转
text.swapcase()
print(text.swapcase())
#将所有单词按a-z升序排序
list1=text.swapcase（）
list1.sort（reverse=False）