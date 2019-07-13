# 利用的是day5的作业，把day5的作业封装进day6的函数中
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



def stats_text_en(text, count): #在第八天基础上那个增加count控制输出
    from collections import Counter #调用Counter计算器
    if not isinstance(text, str):
        raise ValueError('input data is not string type!,again!')
    text = text.replace(',','').replace('.','').replace('--','').replace('*','').replace('!','')#讲非英文字符转化为空
    text = text.lower()#将所有英文字符改为小写
    text = text.split()#以空格拆分独立的单词
    count = int(count) #增加一个int类型变量count
    dir1 = {}
    for i in text: #将字符转换为字典
        count = text.count(i)
        r1 = {i:count}
        dir1.update(r1)

    dir2 = sorted(dir1.items(),key = lambda x:x[1],reverse = True)
    dir2 = Counter(dir1).most_common(count) #按词频排序并用count控制输出
    print(dir2)



def stats_text_cn(text, count): #在第八天基础上那个增加count控制输出
    from collections import Counter #调用Counter计算器
    if not isinstance(text, str):
        raise ValueError('input data is not string type!')
    text = text.replace('\n','').replace('，','').replace('、','').replace(' ','').replace('""','')#删掉换行符，逗号，顿号,空格
    count = int(count) #增加一个int类型变量count
    b1 = {} 
    for i in text: #由字符生成字典
        b1.update({i: text.count(i)})

    b2 = sorted(b1.items(),key = lambda x:x[1],reverse = True)
    b2 = Counter(b1).most_common(count) #按词频排序并用count控制输出
    print(b2)


def stats_text(text, count):
    from collections import Counter #调用Counter计算器
    if not isinstance(text, str):
        raise ValueError('input data is not string type!')
    stats_text_en(text, count) #统计英文单词
    stats_text_cn(text, count) #统计中文单词
        
    
    