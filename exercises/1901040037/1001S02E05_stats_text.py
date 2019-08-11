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



#先把字符串进行切割为list，要调用str类型
elements = text.split()
#定义一个新的list型变量，存储处理过的单词
words = []
#先对文本中要提出的非单词符号搞掉
symbols = ',.*-!'

for element in elements:
    for symbol in symbols:
        #逐个替换字符号，用‘’是为了同时替换字符号所占的位置
        element = element.replace(symbol,'')
    #如果长度不为0，就是可以进入
    if len(element):
        words.append(element)
        
#这就得到了一个剔除了这些的列表
print('正常的英文单词',words)

#初始化一个dict类型变量，用来存放单词出现的次数
counter = {}

#进行去重处理
word_set = set(words)
 
for word in word_set:
     counter[word] = words.count(word)
     
print('英文单词出现的次数',counter)

#2、按照次数从小到大输出
#内置函数sorted的参数key表示暗元素的哪一项的值进行排序
#dict类型的items方法会返回一个包含相应的（key，value）的元组列表
#print('counter.items()',counter.trems)
print('从大到小，排序',sorted(counter.items(),key=lambda x:x[1],reverse=True))

text=text.replace(',',' ').replace('.',' ').replace('--','').replace('!','').replace('*',' ')#将非英文字符替换为空格
text=text.lower()#将所有英文字符改为小写
text=text.split()#以空格拆分为独立的单词
print(text)

zidian = {}

for i in text:  #将字符转换为字典
    count=text.count(i)
    r1={i:count}  #字典自动去重
    zidian.update(r1) 
print(zidian)

zidian1=sorted(zidian.items(),key=lambda x:x[1],reverse=True) #按照单词出现次数，从小到大排序
print(zidian1) 

