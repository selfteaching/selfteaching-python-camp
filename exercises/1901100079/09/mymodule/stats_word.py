from collections import Counter
def stats_text_en(text,count):
    a=text.split()
    b=',.-!*?'
    c=[]
    g=[]
    for x in a:
        for y in b:
            x=x.replace(y,'')
        if len(x): # if len(x) and x.isascii(): 粗犷判断去除中文
            c.append(x)
    for w in c:
        if not'\u4e00'<=w<='\u9fff':
            g.append(w)    
    return Counter(g).most_common(count)

def stats_text_cn(text,count):           
    a=[]
    for b in text:
        if '\u4e00'<=b<='\u9fff':
            a.append(b)
    return Counter(a).most_common(count)    
        
def stats_text(text,count):# 重新定义一个函数把上述两个函数封装为一个函数
    if not isinstance(text,str):
        raise ValueError('无效输入！输入类型：%s'%type(text))
    return stats_text_en(text,count)+stats_text_cn(text,count)# 因为两个函数的返回值都为list，所以可以用+合并在一起'''