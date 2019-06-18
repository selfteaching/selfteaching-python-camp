text1 = '''
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

def stats_text_en(text1):
    elements = text1.split()                      #整理字符
    words = []                                    #给字符列表
    symbols = '*-,.'                              #清理文档中的符号
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')  #把整理好的字符不含符号的加入
        if len(element):                          #字符长度
            words.append(element)
    counter = {}                                  #建立字典
    word_set = set(words)                         #设置字符
    for word in word_set:
        counter[word] = words.count(word)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)
if __name__ =='__main__':
    
    print('英文单词词频降序排列 \n', stats_text_en(text1))

text2 = '''
我相信，若是《自学是门手艺》这本书真的有用，
它的重要用处之一就是能够缓解你的焦虑，让你明白，
首先焦虑没用，其次，有办法也有途径让你摆脱过往一
事无成的状况，逐步产生积累，并且逐步体会到那积累
的作用，甚至最后还能感觉到更多积累带来的加速度…… 
到那时候，焦虑就是 “别人的事情” 了。
'''
def stats_text_cn(text2):
    cn_character=[]
    for character in text2:
        if '\u4e00'<=character<='\u9fff': #查看是否是中文字符
            cn_character.append(character)
    counter={}
    cn_character_set=set(cn_character)
    for character in cn_character_set:
        counter[character] = cn_character.count(character)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)


if __name__ == '__main__':
    
    print('中文汉字字频降序排列 \n', stats_text_cn(text2)) 