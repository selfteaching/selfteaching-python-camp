text = '''
The Zen of python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases arent't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced
In the face of ambxiguity,refuse the temptation to guess
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch
If the implementation is hard to explain,it's a bad idea
If the implementation is easy to explain,it's may be a good idea.
Namespaces are one honking great idea --let's do more of those!
'''

#将字符串样本text里英文单词中包含ea的英文单词剔除
list = text.split()
str1="ea"
str2=[]
for i in list:
    if i.find(str1) < 0:
        str2.append(i)
print(str2)

text=text.replace('better','worse')#better替换成worse
print(text)

text=text.swapcase()#大小写字母转换
print(text)

str2.sort()#将所有单词按a，...z升序排列
print(str2)
