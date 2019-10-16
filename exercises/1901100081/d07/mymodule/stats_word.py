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
# 统计参数中每个英文单词出现的次数，最后返回一个按词频词频降序排列的数组
def stats_text_en(t):
    # 统计次数
    l1=t.split()
    l2=[]
    sy='-*, .''!\n\t:'
    for l3 in l1:
        for sy1 in sy:
            l3 = l3.replace(sy1,'')
            # 用str 类型的isascii 方法判断是否是英文单词
        if len (l3) and l3.isascii():
            l2.append(l3)
    # 排序
    counter={}
    words=set (l2)

    for word in words:
        counter[word]=l2.count(word)
    return (sorted(counter.items(),key=lambda x:x[1],reverse=True))

# 统计汉字
def stats_text_cn(t):
    c=[]
    sy='“”-，。. ‘’!?：」「'
    for c2 in t:
        for sy2 in sy:
            c2=c2.replace(sy2,'')
        if '\u4e00'<=c2<='\u9fff':
            c.append(c2)
    counter ={}
    set2=set(c)
    for c2 in set2:
        counter[c2]=c.count(c2)
    
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)


# 测试

cn='照猫画虎，照葫芦画瓢'

if __name__ =='__main__':  #测试时候为了防止被调用
    e=stats_text_en(text)
    c=stats_text_cn(cn)
    print (e)
    print (c)

# q 为什么还是会把标点符号算进去呢
# a 把英文','换成中文‘，’就可以了


def stats_text(text):
    # n2=[]
    # n1=[]
    # if text >= u'\u4e00' and text <= u'\u9fa5':
        # n1 =stats_text_cn(text )
    # else:
        # n2 =stats_text_en(text  ) # 区分中英文可以直接调用str中的isascii
        # return n1+n2                # 但是为什么用这种方式只能输出英文呢？能用if判断句区分中英文吗
    return stats_text_cn(text) + stats_text_en(text)
    
if __name__ =='__main__ ':  
    ns=stats_text(text)
    print(ns)
