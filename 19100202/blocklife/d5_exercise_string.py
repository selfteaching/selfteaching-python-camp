 
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

# better 替换成 worse
text=text.replace('better', 'worse') 
print(text)


#将非英文字符替换为空格
wordText=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ').replace('!',' ')

#以空格拆分为独立的单词
wordList=wordText.split()

 # 剔除包含ea的英文单词
newWordList=[]
for word in wordList:
    if word.find("ea")<0:
        newWordList.append(word)
#单词合并为字符串
newText = ' '.join(newWordList)
print(newText)

#大小写字母转换
newText=newText.swapcase() 
print(newText)

#将所有单词按a，...z升序排列
newWordList.sort()    
print(newWordList) 