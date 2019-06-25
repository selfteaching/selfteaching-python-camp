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

text1 = text.replace(',', '').replace('.', '').replace('--', '').replace('!', '').replace('*', '')  # 去标点
text2 = text1.lower().split()  # 转换为字符串
dic = {}  # 定义字典
for i in text2:
    if i in dic:
        dic[i] = dic[i] + 1  # 遇到同样的字符串就+1
    else:
        dic[i] = 1
print(dic)  # 字典值
dic2 = sorted(dic.items(), key=lambda x:(x[1],x[0]),reverse=True)  # 对字典按值（value）进行从大到小排序
for key in dic2:
    print(key)  # 打印列表


  
#方法二没成功
#items = sorted(items,key=lambda x:(int(x[0]),-int(x[2]))) 
#print '\n'.join([','.join(x) for x in items]) 
