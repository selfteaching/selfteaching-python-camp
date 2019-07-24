 
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

#剔除包含'ea'的英文单词
arr1=[]
arr2=[]
arr1=text.split(" ")
strtemp="ea"
strresult=""
for i,num1 in enumerate(arr1):
    if strtemp not in num1:
        arr2.append(arr1[i])
strresult=" ".join(arr2)

#将better全部替换成worse
strresult=strresult.replace("better","worse")

#大写字母转成小写，小写字母转成大写
strresult=strresult.swapcase()

#所有单词按字母升序排序
arr3=[]
arr4=[]
arr3=strresult.split(" ")
for num2 in arr3:
    arr4.append("".join((lambda x:(x.sort(),x)[1])(list(num2))))
strresult=" ".join(arr4)

#输出结果
print(strresult)

