
def stats_text_en(str1):
    txt1=str1.split()#分割了字符
    list=[]
    a=',.!*'#把这些符号定义给一个变量（其实这个世界上的一切都是变量，你想使用它们第一步都是要把常量定义给它们）
    #让计算机在这一串字符中遍历一次，寻找符号，把不是符号的存在list列表里面（所谓剔除，就是查找一遍要剔除的东西，把要留下的存储起来）
    for i in txt1:#让i遍历一遍txt1
        for l in a:#让l里边一遍a的各种符号
            i=i.replace(l,'')#i用方法重生了，这个方法是把l中所有的符号都替换成''
        if len(i):#此时的i是删除了符号的，如果这个时候长度不为0，说明是单词了
            list.append(i)#把i里面的常量添加到list中
    #print(list)
            
    w={}#初始化一个字典，其实在统计字数的时候是用遍历的方式，用列表的count方法来做的
    listset=set(list)#把list里面的元素都用set这个函数建立一个集合，可为什么要建立集合呢？
    for p in listset:#让p遍历这个集合
        w[p]=list.count(p)#w是个列表，这个列表里面的是p遍历了listset之后，由count统计字符串个数后的值；w[p]这个写法的意思是什么？
    #print(w)
    return sorted(w.items(),key=lambda x:x[1],reverse=True)
print(stats_text_en('asdfads,asdf,faddf.fasd'))
#统计汉字1.遍历文章；2.把各个汉子放在一个库里面,2.1识别是不是中文字符，2.2先键一个库；3.统计汉字个数，4.排序

def stats_text_cn(txt):
    txt3=[]
    for txt2 in txt:
        if ('\u4e00' <= txt2 <= '\u9fa5'):#识别是不是中文字符
            txt3.append(txt2)#如果是加入到txt3这个列表里
    
    #然后该建立一个集合，在集合中统计汉字的个数，最后排序
    m={}#建立一个字典
    wc=set(txt3)
    for s in wc:
        m[s]=s.count(s)#把统计好s里面汉字个数的值装进m字典中
    return sorted(m.items(),key=lambda x:x[1],reverse=True)
print(stats_text_cn('卧槽，这个行不行啊，卧槽，咋办啊，卧槽'))


print(stats_text_cn('撒地方可能是的看法你的。发生的'))

