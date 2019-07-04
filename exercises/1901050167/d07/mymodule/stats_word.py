
def stats_text_en(text):
    for ch in '!,.':
        text=text.replace(ch,"")
    textlist1 = text.split()
    textlist2 = []
    for i in textlist1:
        if i.isascii():
            textlist2.append(i)
    dict1 = {}
    dict1 = dict1.fromkeys(textlist2)
    word_1 = list(dict1.keys())
    for i in word_1:
        dict1[i] = textlist2.count(i)
    dict2 = {}
    dict2 = sorted(dict1.items(),key=lambda d:d[1],reverse=True)
    return dict2

def stats_text_cn(text):
    txt1=[]
    for m in text:
        if '\u4e00'<=m<='\u9fff':
            txt1.append(m)
    counts={}
    txt2=set(txt1)
    for n in txt2:
        counts[n]=txt1.count(n)
    return sorted(counts.items(),key=lambda x:x[1],reverse=True)

def stats_text(text):
    return stats_text_en(text)+stats_text_cn(text)


