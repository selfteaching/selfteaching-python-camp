text ='''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
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
#自己的方法
word = ""
result = []
for item in text:
    if item == ' ':
        result.append(word)    
        word = ''
    elif item == '\n':
        result.append(word)   
        word = ''  
        result.append('\n')     
    elif item.isalpha():   #必须是字母才可以     
        word = word + str(item) 
freq_dict = {}
#先将统计结果存储起来
for item in result:
    if item != '' and item != '\n' and item != ' ':
        if item in freq_dict.keys():
            freq_dict[item] += 1 
        else:
            freq_dict[item]  = 1  
# print(freq_dict)                    
word_count = () 
#先排序后输出
for i in range(len(freq_dict.copy().keys())):
    word_count = ('',0)
    for key in freq_dict.keys():
        if freq_dict[key] > word_count[1]:
            word_count = (key,freq_dict[key])
 #选出来一个就删掉一个，免得重复比较           
    freq_dict.__delitem__(word_count[0])
    # print (word_count)
        
#老师的方法：
elements = text.split()
words = []
symbols = ',.*-!' #这是要删除掉的符号
for element in elements:
    for symbol in symbols:
        #如果某个element中存在symbols中的某个字符，那么久替换为''
        element = element.replace(symbol,'')
        #如果element长度大于零，就正式作为一个单词写入words里面
    if len(element):
        words.append(element)
#创建一个词典用来存储单词和单词出现的次数
counter = {}    
#用set运算排除了words里面重复的元素
word_set = set(words)
for word in word_set:
    counter[word] = words.count(word)
# print(counter)
print(sorted(counter.items(),key = lambda x:x[1],reverse = True))    