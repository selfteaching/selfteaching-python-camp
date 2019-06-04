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
#清除texe里的标点符号
symbol = ",.!-*"
for str in symbol:
    text = text.replace(str,'')
print(text)
#将字符串样本text里英文单词中包含ea的英文单词剔除
symbol = ",.!-*"
for str in symbol:
    text = text.replace(str,'')
print(text)

list = text.split( )#将text的字符串以空格为分割符分割成字符串并赋值给变量list
str1 = "ea"
str2=[]
for i in list:
    if i.find(str1) == -1:#判断单词如果不包含ea则加进新数组
       str2.append(i) #将不包含ea的单词加进新数组str2
       #m = str2.translate(None,str2.punctuation)
print(str2)

#将better全部替换成worse
print("将better全部替换成worse")
pattern = ["better"]
rep = ["worse" if x in pattern else x for x in str2]
print(rep)

#大写字母转成小写，小写字母转成大写
print("大写字母转成小写,小写字母转成大写")
rep2 = text
print(rep2.swapcase())

#将所有单词按a...z升序排序
print("将所有单词按a...z升序排序")
rep2 = sorted(rep)
print(rep2)
