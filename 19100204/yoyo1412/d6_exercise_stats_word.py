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
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
def Englishwords(text):
    text=text.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        text=text.replace(ch," ")
    words=text.split()
    counts={}
    for word in words:#添加词到字典并统计次数
        counts[word]=counts.get(word,0)+1
    items=list(counts.items())
    items.sort(key=lambda x:x[1],reverse=True)
    for i in range(len(counts)):
        word,count=items[i]
        print("{0:<10}{1:>5}".format(word,count))

def Chinesechar(text):
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
    ChineseCharacters=sorted(word_dict.items(),key=lambda x:x[1],reverse=True)
    #print(type(ChineseCharacters[0]))
    for i in range(len(ChineseCharacters)):
        #print(ChineseCharacters[i][0],ChineseCharacters[i][1])
        print("{0:<10}{1:>5}".format(ChineseCharacters[i][0],ChineseCharacters[i][1]))

Englishwords(text)
print("\n")
Chinesechar("这是第六天的作业啦啦啦")
