def Englishwords(text,count):
    if not isinstance(text,str):
        raise ValueError
    text=text.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        text=text.replace(ch," ")
    words=text.split()
    counts={}
    for word in words:#添加词到字典并统计次数
        counts[word]=counts.get(word,0)+1
    '''items=list(counts.items())
    items.sort(key=lambda x:x[1],reverse=True)
    for i in range(len(counts)):
        word,count=items[i]
        print("{0:<10}{1:>5}".format(word,count))'''
    print(Counter(counts).most_common(count))

def Chinesechar(text,count):
    if not isinstance(text,str):
        raise ValueError
    word_list=[]
    word_dict={}
    exstr="，。！？、（）【】<>《》=：+-*—“”…"
    for line in text:#添加字到列表
        for char in line:
            word_list.append(char)
    for char in word_list:#统计字频
        if char not in exstr:
            if char.strip() not in word_dict:
                word_dict[char]=1
            else:
                word_dict[char]+=1
    #ChineseCharacters=sorted(word_dict.items(),key=lambda x:x[1],reverse=True)
    #print(type(ChineseCharacters[0]))
    #for i in range(len(ChineseCharacters)):
        #print(ChineseCharacters[i][0],ChineseCharacters[i][1])
        #print("{0:<10}{1:>5}".format(ChineseCharacters[i][0],ChineseCharacters[i][1]))
    print(Counter(word_list).most_common(count))
