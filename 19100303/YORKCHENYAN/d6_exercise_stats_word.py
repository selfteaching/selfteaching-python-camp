texten = '''
The Zen of Python, by Tim Peters

Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex.
Complex is better than complicated. Flat is better than nested.
Sparse is better than dense. Readability counts.
Special cases aren't special enough to break the rules. Although practicality beats purity.
Errors should never pass silently. Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those! '''




textcn = '''
今天下午晚些时候美方代表团抵达北京，今晚双方将举行工作晚餐，明天双方将全天进行磋商。
下周刘鹤副总理将访问华盛顿与美方举行第九轮中美经贸高级别磋商，目前双方团队正在全力以赴进行认真谈判，朝着落实两国元首重要共识的方向努力。'''




def status_text_en(text):

   
    #进行分割
    textsplit=text.split()

    #去除标点符号
    i=0
    while i<len(textsplit):
        textsplit[i]=textsplit[i].strip(',*-.!')
        if textsplit[i]=='': 
            textsplit.remove('')
        else:
            i=i+1

    print(textsplit)


    textDict={}
    for i in range(len(textsplit)):
        textDict[textsplit[i]]=0
    for i in range(len(textsplit)):
        textDict[textsplit[i]]=textDict[textsplit[i]]+1

    print(textDict)   

    R_dict = sorted(textDict.items(),key=lambda item:item[1],reverse=True)
    print(R_dict)
    return R_dict



def status_text_cn(text):

   
    #进行分割
    textsplit={}
    for i in text: 
        if u'\u4e00' <= i <= u'\u9fa5':
            textsplit[i]=text.count(i)

    R_dict = sorted(textsplit.items(),key=lambda item:item[1],reverse=True)

    return R_dict


endict= status_text_en(texten)
print(endict)


cndict= status_text_cn(textcn)
print(cndict)

