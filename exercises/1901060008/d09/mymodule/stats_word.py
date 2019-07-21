from collections import Counter
import re # 调用正则表达式模块
t= '''
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
美丽总比丑陋好。
显式比隐式好。
简单总比复杂好。
复杂总比复杂好。
平的比嵌套的好。
稀疏总比密集好。
可读性。
特殊情况还不足以打破规则。
虽然实用性胜过纯洁性。
错误不应该悄无声息地过去。
除非显式地沉默。
面对敏锐，拒绝猜测的诱惑。
应该有一种——而且最好只有一种——显而易见的方法来做到这一点。
不过，除非你是荷兰人，否则这种方式一开始可能并不明显。
现在总比不做好。
虽然从来没有比“现在”更好。
如果实现很难解释，这是一个坏主意。
如果实现很容易解释，这可能是一个好主意。
名称空间是一个很棒的主意——让我们做更多这样的事情!
'''

def stats_text_en(text,count):          #定义统计英文字符的函数
    t=type(text)                  #判断输入的参数类型
    if t ==str:                   #利用判断语句进行分析
        for i in '.'',''-''*''!''?''。':      #利用for循环去掉标点符号
            text=text.replace(i,' ')
            
        text=text.lower()     #把字符串统一为小写字母
        t1= re.sub("[^A-Za-z]", " ", text)    # 利用正则表达式提取英文字符re.sub(pattern, repl, string, count=0, flags=0)
        
        t2=t1.split()              #拆分提取出来的英文字符串
        t3=Counter(t2)
        count=Counter(t2).most_common(count)
        print('打印英文的排序列表：\n',t3)
        print('按出现次数大小将前五的单词打印:\n',count)
        print()   
    else:
         print(f'ValueError,you are enter {t}, please enter string')
    
        
          
def stats_text_cn(text,count):        #定义统计中文字符的函数
    t=type(text)
    if t ==str:

        t1=re.findall(r'[\u4e00-\u9fa5]',text)    #利用正则表达式按unicode编码将中文提取出来
        t2=Counter(t1)
        count=Counter(t1).most_common(count)
        print('打印中文排序:\n',t2)
        print('按出现次数大小将前五的中文打印：\n',count)
       
    else:
         print(f'ValueError,you are enter {t}, please enter string')
       
def stats_text(text,count):         #定义一个主函数，后续直接调用它就行了
    t=type(text)
    if t ==str:
        stats_text_en(text,count)       #把统计英文的函数放进来，作为它的子函数
        stats_text_cn(text,count)       #把统计中文的函数也放进来，作为它的子函数
        
    else:
        print(f'ValueError,you are enter {t}, please enter string')
        
stats_text(t,5)        #调用主函数