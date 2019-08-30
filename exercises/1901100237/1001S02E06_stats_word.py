def stats_text_en(text):
    texts = text.split()
    aa = []
    c = '+, -， *, /, &, %, ?, !'
    for a in texts:
        for cc in c:
            a = a.replace(cc,'')
        if len(a):
            aa.append(a)
        d = {}
        z = set(aa)
    for v in z:
        d[v] = aa.count(v)
    print('输出结果 ==>', sorted(d.items(), key=lambda x: x[1], reverse=True))
    return
    #将文本text中英文单词出现次数统计并按词频降序输出
from html.parser import HTMLParser
def stats_text_cn(text):
    texts = text.split()
    aa = []
    for a in texts:
        if len(a):
            aa.append(a)
        d = {}
        z = set(aa)
    for v in z:
        d[v] = aa.count(v)
    print('输出结果 ==>', sorted(d.items(), key=lambda x: x[1], reverse=True))
    return
    #将文本text中汉字出现次数统计并按词频降序输出
