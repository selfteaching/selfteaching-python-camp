text_en='''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than compalicated.
Flat is better than nested.
Sprase is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicity silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
text_cn='给函数定义有可变数目的参数也是可行的。这里有三种形式，可以组合使用。'


def stats_text_en(text):
    elemets=text.split()
    '''将文档中的句子转为分隔开的单词
    
    方便后面的处理'''
    words=[]   #建立要用的单词列表
    symbols=',.*-!'
    for elemet in elemets:                        #      
        for symbol in symbols:                    #
            elemet=elemet.replace(symbol,'')      #
        if len(elemet):                           #
            words.append(elemet)                  #此步骤剔除words列表中的标点符号

    counter={}
    text_set=set(words)
    for word in text_set:
        counter[word]=words.count(word)
    print(sorted(counter.items(),key=lambda x: x[1],reverse=True))
    '''用dict类型的列表可同时存放单词及其出现的频数
    
    然后按频数大小排序并打印出结果
    
    reverse=True使结果降序输出'''

stats_text_en(text_en)     #使用时直接在括号内写入需要操作的str类型文档即可

def stats_text_cn(text):
    characters=[]
    symbols='，。'
    text_list=list(text)
    '''试验时发现无法用.split方法对汉字进行分隔

    所以改用list（）达到分隔开每个字的效果'''
  #
    for zi in text_list:
        for symbol in symbols:
            zi=zi.replace(symbol,'')
        if len(zi):
            characters.append(zi)
  #上面这个部分还是用于剔除标点符号
    counter={}
    characters_set=set(characters)
    for character in characters_set:
        counter[character]=text_list.count(character)
    print(sorted(counter.items(),key=lambda x:x[1], reverse=True))
    '''最后的排序及输出结果与英文相同
       也可以在使用函数时再打印
       记得在最后一行把print()删除即可'''

stats_text_cn(text_cn)       #