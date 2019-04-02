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

#1.将better全部替换成worse
#2.从上一步结果里，将单词中包含ea的单词剔除
#3.将上一步结果里的大写字母转成小写，小写字母转成大写
#4.将上一步结果里所有单词按a...z升序排列，输出结果


text=text.replace('better', 'worse') # 将 better 替换成 worse
print(text)

text1=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ') #替换分隔符为空格
text2=text1.split( )#切成单词
EA=[]

for i in text2:
    if i.find('ea')>0:
        EA.append(i)
print(EA)


for j in range(len(EA)):
    text=text.replace(EA[j]+' ', '')
print(text)

text=text.swapcase()
print(text)

text=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ') #替换分隔符为空格
text=text.split( )#分隔字符串

print(text)

text.sort()
print(text)

dict={}
for it in text:
    if it not in dict:
       dict[it] = 1
    else: dict[it] += 1
dict = sorted(dict.items(),key=lambda x:x[1],reverse=True)
print(dict)