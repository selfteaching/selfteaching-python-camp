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
'''

string=text.replace(',',' ').replace('--',' ').replace('*',' ').replace('!',' ').replace('.',' ')
string1=string.lower()#Python lower() 方法转换字符串中所有大写字符为小写。
#print(string1)
string2=string1.split()
#print(string2)
string3={}#字典数据类型，创建一个空字典
for a in string2:
   count=text.count(a)#Python count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
   text_count={a:count}
   string3.update(text_count)
#print(string3)

string3=sorted(string3.items(),key=lambda a:a[1],reverse=True)
print(string3)
#方法二
import  re 
import  collections  
def  stats_text_en(text):
    a=re.sub(r'[^A-Za-z]',' ',text)    #只取英文单词
    newlist=a.split()                      #单词划分
    return(collections.Counter(newlist))  #输出英文单词频数统计结果
print(stats_text_en(text))
 