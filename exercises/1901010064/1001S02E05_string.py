#打开调取文本文件
f1 = open("text.txt","r")
content= f1.read()
f1.close()

import string
translator = str.maketrans('', '', string.punctuation)
z=content.translate(translator)


#替换单词
t1=z.replace("better","worse")
with open("text.txt","w") as f2:
    f2.write(t1)

#剔除ea
list1=t1.split()
list2=[]
str1="ea"
for t1 in list1:
    if str1 not in list1:
        list2.append(t1)


a=[str(i) for i in list2 ]
b=" ".join(a)

#字母进行大小写翻转
c=b.swapcase()
d=c.upper()


#所有单词按a-z顺序排
e=(d.split(" "))
print(e)
print(sorted(e, key=str.lower))