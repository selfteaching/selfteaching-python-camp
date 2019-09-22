text = '''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is beter than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiquity, refuse the temptation to quess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
if the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

#将better全部替换成worse
text=text.replace('better','worse')
print(text)

#大写字母转换成小写，小写字母转换成大写
text=text.swapcase()
print(text)


#将字符串样本text里英文单词中包含ea的英文单词剔除
text=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')#将非英文字符替换为空格
text=text.split()
temp1="ea" 
temp2=[]
for i in text:
    if i.find(temp1)<1:
        temp2.append(i)
print(temp2)

#将所有单词按a...z的升序排列
temp2.sort()
print(temp2)