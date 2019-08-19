def stats_text_en(txt):
    txt1=txt.split()#分割了字符
    list=[]
    a=',.!*'#把这些符号定义给一个变量（其实这个世界上的一切都是变量，你想使用它们第一步都是要把常量定义给它们）
    #让计算机在这一串字符中遍历一次，寻找符号，把不是符号的存在list列表里面（所谓剔除，就是查找一遍要剔除的东西，把要留下的存储起来）
    for i in txt1:#让i遍历一遍txt1
        for l in a:#让l里边一遍a的各种符号
            i=i.replace(l,'')#i用方法重生了，这个方法是把l中所有的符号都替换成''
        if len(i):#此时的i是删除了符号的，如果这个时候长度不为0，说明是单词了
            list.append(i)#把i里面的常量添加到list中
    #print(list)
            
    #初始化一个字典，其实在统计字数的时候是用遍历的方式，用列表的count方法来做的
    w={}
    listset=set(list)
    for p in listset:
        w[p]=list.count(p)
    return sorted(w.items(),key=lambda x: x[1],reverse=True)


#目的：把遍历出来的词放在一个字典里，怎么判定是汉子呢？然后统计，然后排列
def stats_text_cn(txt2):
    e=[]
    for r in txt2:
        if '\u4e00' <= r <= u'\u9fff':
            e.append(r)
    t={}#定义个字典
    y=set(e)#建立一个集合，因为集合才能统计
    for u in y:
        t[u]=e.count(u)
    return sorted(t.items(),key=lambda x: x[1],reverse=True)


def stats_text(text):
    
    return stats_text_en(text) + stats_text_cn(text)
