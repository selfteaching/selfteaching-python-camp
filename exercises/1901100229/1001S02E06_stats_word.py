#1.封装统计英文字频的函数 
en_text = '''
The Zen of Python , by Tim Peters

Beautiful is better than ugly.
Explicit is better than implcit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases are't special enough to break the rules.
Although practicality beats purity.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one --- and preferably only one -- obvious way to do it.
Although the way may not be obvious at first unless you are a Dutch.
Now is better than never.
Although never is better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it's maybe a good idea.
Namespaces are one honking great idea --- let's do more of those!
'''

def stats_text_en(text):       #定义一个名为stats_text_en，接收text为参数的函数
    symbols = '~!@#$%^&*(),.[]{}|?/;<>'   
    for i in symbols:
        text=text.replace(i, ' ')     #通过for...in...循环，把所有可能出现的特殊字符都替换成空格
    text=text.lower()      #所有字母变成小写
    text=text.split()      #文本转列表
    dict1={}               #新建一个空字典
    for i in text:          #指定i遍历text中的元素
        j=text.count(i)     #统计text中各单词的数量，这一步可以优化，因为有些单词出现了不止一遍，相当于同一个单词统计了好几遍
        dict2={i:j}          
        dict1.update(dict2)
    return sorted(dict1.items(),key=lambda x:x[1],reverse=True)
  

print(stats_text_en(en_text))


#2.封装统计中文汉字字频的函数 
cn_text = '''                       
美丽胜过丑陋。
显式优于隐式。
简单比复杂更好。
复杂比复杂更好。
优于嵌套。
稀疏优于密集。
可读性很重要。
特殊情况不足以打破规则。
虽然实用性胜过纯洁。
错误不应该默默地传递。
除非明确沉默。
面对困惑，拒绝猜测的诱惑。
应该有一个 - 最好只有一个 - 明显的方法来做到这一点。
虽然这种方式起初可能并不明显，除非你是荷兰人。
现在比永远好。
虽然现在永远不会比*正确好。
如果实施很难解释，这是一个坏主意。
如果实现很容易解释，那可能是个好主意。
命名空间是一个很棒的主意 - 让我们做更多的事情吧！
'''

def stats_text_cn(text):    #定义一个名为stats_text_cn，接受text为参数的函数
    dict_1={} 
    for i in text:
        if u'\u4e00' <= i <= u'\u9fff':#使用正则表达式判断是不是中文
            count = text.count(i)
            dict_2 = {i:count}
            dict_1.update(dict_2)
    return sorted(dict_1.items(),key=lambda item:item[1],reverse = True) 
    
print(stats_text_cn(cn_text)) #调用函数并打印结果

 