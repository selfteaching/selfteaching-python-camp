#打开调取文本文件
f1 = open("test.txt","r")
content= f1.read()
f1.close()
#删除文本文件所有符号
import string
translator = str.maketrans('', '', string.punctuation)
z=content.translate(translator)
#转为列表
a=z.split()




#用字典统计各个单词使用次数
#列表转为集合，去除重复项
set1=set(a)

#集合转为列表
b=list(set1)


#新建空字典
dir1={}

for x in range(len(b)):
    dir1[b[x]]=0
    for y in range(len(a)):
        if b[x] ==a[y]:
            dir1[b[x]]+=1


#按出现次数从大到小输出所有单词和次数
dir2=sorted(dir1.items(), key=lambda d:d[1], reverse = True)  
print(dir2)

