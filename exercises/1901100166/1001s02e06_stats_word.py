 #统计英文单词出现次数
def stats_text_en(a):
    A=a.split()   
    B=[]   
    C=',.*-!'

    for AA in A:  
        for CC in C:  
            AA=AA.replace(CC,'') 
        if len(AA):
            B.append(AA)
    counter={}  
    B_set=set(B)  

    for BB in B_set:
        counter[BB]=B.count(BB)  
    #函数返回值用return进行返回，如果没有return，则返回值为none
    return sorted(counter.items(),key=lambda x: x[1],reverse=True)
    #在一个完整的文件里是不能用return值，在函数里可以用？
 
 
 #统计中文汉字次数

def cn(b):
    cn_character=[]
    for character in b:
        if'\u4e00'<=character<='\u9fff':  #汉字在unicode中都有对应固定的值
            cn_character.append(character)
    counter={}
    cn=set(cn_character)
    for character in cn:
        counter[character]=cn_character.count(character)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)



a= '''
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



b='我爱北京天安门！'

#if __name__ == "__main__":  #这个公式作用：防止在引用这个文件时不运行此代码

print('英文次数==>\n',stats_text_en(a))
print('中文次数==>\n',cn(b))