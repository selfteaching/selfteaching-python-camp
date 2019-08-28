def stats_text_en(text):
    aa = []
    c = '+, -， *, /, &, %, ?, !'
    for a in text:
        for cc in c:
            a = a.replace(cc,'')
        if len(a):
            aa.append(a)
        d = {}
        z = set(aa)
    for v in z:
        d[v] = aa.count(v)
    print('输出结果 ==>', sorted(d.items(), key=lambda x: x[1], reverse=True))
#将文本text中的英文单词出现次数统计并按词频降序输出


def stats_text_enm(text):
    aa = []
    c = '+, -， *, /, &, %, ?, !'
    for a in text:
        for cc in c:
            a = a.replace(cc,'')
        if len(a):
            aa.append(a)
        d = {}
        z = set(aa)
    for v in z:
        d[v] = aa.count(v)
    print('输出结果 ==>', sorted(d.items(), key=lambda x: x[1], reverse=True))
#中文版