# 利用的是day5的作业，把day5的作业封装进day6的函数中
t = '''
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
import re #调用正则表达式模块
          # re.sub(pattern, repl, string, count=0, flags=0)
def stats_text_en(t_en):  #定义函数
    if not isinstance(t_en,str):
        raise ValueError('输入的不是文本格式，请重新输入：') #isinstance(object, classinfo) 判断函数 object，对象   classinfo，类型
    m = t_en.replace(',','').replace('.','').replace(':','').replace(';','').replace('"','').replace('!','').replace('?','').replace('、','').replace('，','').replace('。','').replace('”','').replace('：','').replace('；','').replace('\n','').replace('！','').replace('？','').replace('/','').replace('*',' ').replace('--',' ')
    m = m.lower() #全英文单词小写
    m = re.sub("[^A-Za-z]", " ", m)   # 借用了这个正则表达式，这里保留了英文单词，^代表取出大小写a-z以外所有的字符串剔除
    m = m.split()
    n = {}
    for i in m:
        count = m.count(i)
        r1 = {i:count}
        n.update(r1)
    c = sorted(n.items(),key=lambda x:x[1],reverse=True)
    print('英文单词统计频率如下： \n',c) # 这里print()函数缩进就是封装进我定义的函数里面去了

def stats_text_cn(t_cn):
    if not isinstance(t_cn,str):
        raise ValueError('输入的不是文本格式，请重新输入：')
    o = t_cn.replace(',','').replace('-',' ').replace('.','').replace(':','').replace(';','').replace('"','').replace('!','').replace('?','').replace('、','').replace('，','').replace('。','').replace('“','').replace('”','').replace('：','').replace('；','').replace('\n','').replace('！','').replace('？','').replace('/','').replace('*',' ').replace(' ','')
    o = re.sub("[A-Za-z0-9]", "",o) #借用了这个正则表达式，这里删除了英文单词，因为没有加上^
    p = {}
    for j in o:
        count = o.count(j)
        r2 = {j:count}
        p.update(r2)
    q = sorted(p.items(),key=lambda x:x[1],reverse=True)
    print('中文字统计频率如下： \n',q)


#分别调用stats_text_en和stats_text_cn，输出合并词频统计结果
def stats_text(en_cn):
    '''中英文词频统计'''
    if not isinstance(en_cn,str):
        raise ValueError
    en_cn = ((stats_text_cn(en_cn), stats_text_en(en_cn)))
stats_text(t)
    

