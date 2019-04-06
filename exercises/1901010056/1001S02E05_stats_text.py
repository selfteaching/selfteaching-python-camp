text = ''' The Zen of Python, by Tim Peters
Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambxiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those! '''
 
textlist1 = text.split() #形成单词列表
textlist2 = []             #列表推导用方括号（“[]”）括起来
for i in textlist1:              #对textlist1中的每个i都进行检测
    if i.isalpha():               #如果i是字母，则附加在textlist2里面
        textlist2.append(i)      #去除非单词
dict1 = {}                         #标准的映射类型字典。字典的键几乎是任意值
dict1 = dict1.fromkeys(textlist2)  #对dict1改变成键值来自于textlist2
word_1 = list(dict1.keys())        #赋值world_1是表dict1的键值
for i in word_1:                    #对于每个在world_1里的i都进行遍历
    dict1[i] = textlist2.count(i)   #统计单词出现的次数 ，dict1里面的i，等于在textlist2中出现的次数
dict2 = {}                           #让dict2等于{}
dict2 = sorted(dict1.items(),key=lambda d:d[1],reverse=True)  #按values进行排序，#sort(*, key=None, reverse=False)此方法会对列表进行原地排序，只使用 < 来进行各项间比较
dict2 = dict(dict2)                  #转化为字典                #true注意是大写
print(dict2)