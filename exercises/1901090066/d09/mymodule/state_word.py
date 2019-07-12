from collections import Counter

def stats_text_en(tx1,count):
    # 将符号变为空格，将字符串分割
    if not isinstance(tx1,str):#如果不是字符串，则抛出异常
        raise ValueError("输入的不是字符串类型!")
    text0=[]
    txt= tx1.replace('\n', ' ').replace('.', ' ').replace('：', ' ').replace('--', ' ').replace('.',' ').replace('*',' ').replace('「',' ').replace('」',' ')
    txt1=txt.split()
    for i in txt1:
        if i >'\u9fff' or i<'\u4e00':
            text0.append(i)
    count=int(count)
    return Counter(text0).most_common(count)


def stats_text_cn(tx2,count):
    # 将text中符号变为空格，然后放到list中
    if not isinstance(tx2,str):#如果不是字符串，则抛出异常
         raise ValueError("输入的不是字符串类型!")
    count=int(count)    
    cn_characters=[]
    for i in tx2:
        if '\u4e00'<=i<='\u9fff':
            cn_characters.append(i)
    return Counter(cn_characters).most_common(count)

def stats_text(txx,count): #定义函数，分别调⽤stats_text_en , stats_text_cn ，输出合并词频统计结果
    if not isinstance(txx,str):#如果不是字符串，则抛出异常
         raise ValueError("输入的不是字符串类型!")
    result = stats_text_en(txx,count) + stats_text_cn(txx,count)
    return result 


