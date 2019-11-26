text = '''
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
import re
import collections
def stats_text_cn(text):
    p=re.compile(u'[\u4e00-\u9fa5]') #匹配一组字符可以用方括号[]定义自己的字符分类。
    a=re.findall(p,text)  #找到text中匹配中文u'[\u4e00-\u9fa5]'
                          #re.findall遍历匹配，可以获取字符串中所有匹配的字符串，返回一个列表。            
    str=''.join(a) # ''.join()是字符串操作函数，常常用于字符连接操作。把list列表转为str字符串
    print(collections.Counter(str)) #统计中文词频

def stats_text_en(text):
    b=re.sub(r'[^A-Za-z]',' ',text) #用正则表达式过滤出26个大小写英文字母。text中非字母的替换成空格。
    list=b.split() #以空格分割，返回分割后字符串列表。
    print(collections.Counter(list)) #统计单词词频

def stats_text(text):     
        stats_text_cn(text)
        stats_text_en(text)
 