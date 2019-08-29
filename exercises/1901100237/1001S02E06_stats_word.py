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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
dd = '''两次读后感发技术啊UI士大夫好啊啊UI儿很过分 啊哎啊 阿尔UI维护费水电费就怕瓮福五发放阿牛瓮福
 为预防噶愈发而富啊饿哦也埃尔文风格也发过安抚过夜费过安慰法为风月法国与阿尔王府好亚尔福娃vudsiuvui
 按时到货VGA与五色饭会计师对话而无任何衣阿华斯eruptYui阿斯u噶贵妃法务发都是 GV阿越挖 fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck 
 '''



def stats_text_en(text):
    aa = []
    c = '+, -， *, /, &, %, ?, !, q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h, j, k, l, z, x, c, v, b, n, m, Q, W, E, R, T, Y, U, I, O, P, A, S, D, F, G, H, J, K, L, Z, X, C, V, B, N, M, \n, .'
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
    return
#将文本text中的汉字出现次数统计并按词频降序输出
stats_text_en(text)