#Selflearning day5 homework Part1 ,handling string!

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

#将 better全部替换成 worse
t1=text.replace('better', 'worse')
print(t1)

#将字符串样本text里英文单词中包含"ea"的英文单词剔除
t2=t1.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ') #将非英文字符替换为空格
t3=t2.split() #将str 转成list 

t4=[]
for i in t3:
    if i.find("ea")==-1: #在数组里寻找“ea”单词位置 ，剔除带“ea”单词
        t4.append(i)
print(t4)

t5=[]
for i in t4:
    a=i.swapcase() #大写字母转换成小写，小写字母转换成大写
    t5.append(a)
print(t5)

t5.sort() #将所有单词按a...z的升序排列
print(t5)

####整合


            
