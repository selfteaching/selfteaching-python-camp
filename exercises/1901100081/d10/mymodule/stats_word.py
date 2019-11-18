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
def stats_text_en(t,co=100):
    # if type(t)!=str:
        # raise ValueError('非字符串类型')
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
    from collections import Counter
    cnt = Counter()
    for word in l2:
        cnt[word] += 1
    return (cnt.most_common(co))

# 统计汉字
def stats_text_cn(t,co = 20):
    if type(t)!=str:
        raise ValueError('非字符串类型')
    c=[]
    sy='“”-，。. ‘’!?：」「'
    for c2 in t:
        for sy2 in sy:
            c2=c2.replace(sy2,'')
        if '\u4e00'<=c2<='\u9fff':
            c.append(c2)
    str1=''.join(c)
    import jieba 
    seg_list = jieba.cut(str1,cut_all=False)
    # print("defauil mode:"+"/".join(seg_list))
    from collections import Counter
    cnt = Counter()
    c3=[]
    for word in seg_list:
        cnt[word] += 1
        if len(word)>1:
            c3.append(word)
           # for word in c:
        # cnt[word] += 1
    return (Counter(c3).most_common(co))
  
    # counter ={}
    # set2=set(c)
    # for c2 in set2:
        # counter[c2]=c.count(c2)
    
    # return sorted(counter.items(),key=lambda x:x[1],reverse=True)

# 汉字和英文
def stats_text(text):
    if type(text)!=str:
        raise ValueError('非字符串类型')
    return stats_text_cn(text) + stats_text_en(text)

# 测试

cn='照猫画虎，照葫芦画瓢。这里应该有一个长文本，但是我也不知道该写一个什么样的长文本，就打算写个流水账先试一试。'
if __name__ =='__main__':  #测试时候为了防止被调用
    e=stats_text_en(text)
    cx =stats_text_cn(cn)
    print (e)
    print (cx)

# q 为什么还是会把标点符号算进去呢
# a 把英文','换成中文‘，’就可以了

