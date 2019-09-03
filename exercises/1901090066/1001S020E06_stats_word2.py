text='''
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
def stats_text_cn(text):
    # 将text中符号变为空格，然后放到list中
    txt= text.replace('\n', '').replace('。', '').replace('！', '').replace('--', '').replace('，','')
    list=[]
    for i in txt:
        list.append(i)
    counts = {}
    # 如果字典里再次出现该单词，次数加一，否则次数为一
    for text in list:
        if text in counts.keys():
            counts[text] = counts[text] + 1
        else:
            counts[text] = 1
    #排序，从高到低
    count_text=sorted(counts.items(),key=lambda x:x[1],reverse=True)
    return count_text
print (stats_text_cn(text))