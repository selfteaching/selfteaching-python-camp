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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''               # 需添加三重三引号确定文本内容范围
import re                           #   替换字符串
a = re.sub('better','worse',text)   
                                    #   替换包含ea的字符串
list = text.split()                 #   将text中的字符串分列入表 
text1 = []                          #   创建新表 text1
for i in list:
    if 'ea' not in i:
        text1.append(i)              #   遍历表，将不包含ea的内容加入新表text1
    else:
        pass
text = ' '.join(text1)               #   将新表内容转换为STR                                

                                    #翻转大小写
c = text.swapcase()
list = text.split()
print(r'',sorted(c.split()))          #  a-z 升序排列