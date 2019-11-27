
def stats_text_en(text):
    if not isinstance(text,str):                #加入的类型判断，判断a是否是str类型
        raise ValueError('参数必须是str类型，输入类型%s' % type(text))
     
    A=text.split()   
    B=[]   
    C=',.*-!'

    for AA in A:  
        for CC in C:  
            AA=AA.replace(CC,'') 
        if len(AA) and AA.isascii():   #用str型的isascii方法判断是否是英文单词
            B.append(AA)
    counter={}  
    B_set=set(B)  
    for BB in B_set:
        counter[BB]=B.count(BB)  
    return sorted(counter.items(),key=lambda x: x[1],reverse=True)
  
 

def cn(text):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型，输入类型%s' % type(text))
    cn_character=[]
    for character in text:
        if'\u4e00'<=character<='\u9fff':  
            cn_character.append(character)
    counter={}
    cn=set(cn_character)
    for character in cn:
        counter[character]=cn_character.count(character)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)

def stats_text(text):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型，输入类型%s' % type(text))
    '''
    合并 英文词频和 中文字频的结果
    '''
    return stats_text_en(text)+cn(text)




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