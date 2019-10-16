

def stats_text_en(text):
    # 将符号变为空格，将字符串分割
    text0=[]
    txt= text.replace('\n', ' ').replace('.', ' ').replace('：', ' ').replace('--', ' ').replace('.',' ').replace('*',' ').replace('「',' ').replace('」',' ')
    txt1=txt.split()
    for i in txt1:
        if i >'\u9fff' or i<'\u4e00':
            text0.append(i)
    counts = {}
    # 如果字典里再次出现该单词，次数加一，否则次数为一
    for text in text0:
        if text in counts.keys():
            counts[text] = counts[text] + 1
        else:
            counts[text] = 1
    #排序，从高到低
    count_text=sorted(counts.items(),key=lambda x:x[1],reverse=True)
    return count_text


def stats_text_cn(text):
    # 将text中符号变为空格，然后放到list中
    list=[]
    for i in text:
        if '\u4e00'<=i<='\u9fff':
            list.append(i)
    counts = {}
    # 如果字典里再次出现该单词，次数加一，否则次数为一
    for i in list:
        if i in counts.keys():
            counts[i] = counts[i] + 1
        else:
            counts[i] = 1
    #排序，从高到低
    count_text=sorted(counts.items(),key=lambda x:x[1],reverse=True)
    return count_text
def stats_text(text): #定义函数，分别调⽤stats_text_en , stats_text_cn ，输出合并词频统计结果
    result = stats_text_en(text) + stats_text_cn(text)
    return result 


text='''
The Zen of Python, by Tim Peters.


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

美胜于丑。
显式优于隐式。
简单胜于复杂。
复杂总比复杂好。
稀疏胜于稠密。
可读性计数。
特殊情况不足以打破规则。
尽管实用性胜过纯洁性。
错误永远不会悄悄地过去。
除非明确沉默。
面对悠闲，拒绝猜测的诱惑。
应该有一种--最好只有一种--显而易见的方法
它。
不过，如果不是荷兰语的话，这种方式一开始可能并不明显。
现在总比没有好。
虽然从来没有比现在更好。
如果实现很难解释，那是个坏主意。
如果实现很容易解释，这可能是一个好主意。
名称空间是一个非常好的主意——让我们做更多的事情吧！
'''
#if __name__ == "__main__":
    #result=stats_text(text)
    #print('统计==>\n',result)