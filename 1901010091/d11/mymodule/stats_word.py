
def stats_text_en(text,count):
    t1=text.split()#将字符串转化为列表
    word=[]
    #去除非英文字符
    import re
    for i in t1:#历遍列表t1
        s=re.findall(r'[^a-zA-Z]+',i)#找出t1中的非英文字符
        for j in s:#j历遍所有非英文字符
            i=i.replace(j,'')#i中所有非英文字符用空白替换
        if len(i):#如果i是英文字符串
            word.append(i)#将i加入word中
    #统计词频
    cou={}
    w1=set(word)
    w2=list(w1)
    for a in range(len(w2)):
        cou[w2[a]]=0
        for b in range(len(word)):
            if w2[a]==word[b]:
                cou[w2[a]]+=1
    import collections
    yy=collections.Counter(cou).most_common(count)
    print(yy)

def stats_text_cn(text,count):
    word_lst=[]
    word_dict={}
    
    import jieba
    seg_list=jieba.lcut(text,cut_all=False)
    text_jb=format(seg_list)

    exclude_str="，］’ ［。！!?？、APPcontents' {},:type ,author\（）title【】id《》,.<>=：+-*——“”...%1234567890a10bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQURSTUVWXYZ"
    
    textin=text_jb.split()
    textout=[]
    #添加每一个字到列表中
    for line in textin:
        for char in line:
            word_lst.append(char)

    #用字典统计每个字出现的次数
    for char in seg_list:
        if char not in exclude_str:
            if len(char)>1:
                if char.strip() not in word_dict:#去除各种空白
                    word_dict[char]=1
                else:
                    word_dict[char]+=1
    #按字频排序
    import collections
    textout=collections.Counter(word_dict).most_common(count)
    
    stats_text_cn.textout=textout
    #输出结果
    print(textout)

def stats_text(text,count):
    if type(text)!=str:
        raise ValueError("文本为非字符串")
    stats_text_en(text,count)
    stats_text_cn(text,count)
   