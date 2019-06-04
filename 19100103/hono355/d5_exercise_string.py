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
#将字符串样本text里英文单词中包含ea的英文单词剔除
textlist = text.split()#将text的字符串以空格为分隔符分割成字符串并赋值
str1 = 'ea'
str2 = []
for i in textlist:
    if i.find(str1) == -1:#筛选出不含ea的单词
        str2.append(i)
print(str2)

#将better全部替换成worse
str3 = ['worse' if i == 'better' else i for i in str2]
print(str3)

#将大写字母转成小写，小写字母转成大写
def all_lower(str3):
    return [i.lower() for i in str3]#将大写字母转成小写
print(all_lower(str3))

def all_upper(str3):
    return [i.upper() for i in str3]#将小写字母转成大写
print(all_upper(str3))

#将所有单词按a...z升序排列
str4 = sorted(str3)
print(str4)