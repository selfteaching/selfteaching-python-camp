def stats_text_en(text):
    elements=text.split()
    words=[]
    symbols=',.*-!'
    for element in elements:
        for symbol in symbols:
            element =element.replace(symbol,'')
        if len(element):
           words.append(element)
    counter={}
    word_set=set(words)
    for word in word_set:
       counter[word] =words.count(word)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)

def stats_text_cn(text):
    cn_characters=[]
    for character in text:
        if '\u4e00' <=character<='\u9fff':
            cn_characters.append(character)
    counter={}
    cn_characters_set=set(cn_characters)
    for character in cn_characters_set:
        counter[character]=cn_characters.count(character)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)

en_text = ''' 
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
Now is better than never. Although never is often better than *right* now. 
If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain,
it may be a good idea. Namespaces are one honking great idea -- let's do more of those!
'''

cn_text='''
昨天上午，根据导航显示的“玉泉路1号”，
我来到植物园北门的一处停车场附近，
来回找了十来分钟都没找到“故居”。
植物园内的指路牌，
也没有任何蔡元培故居的标志或提示。
询问停车场工作人员，一连问了五人，无论是“玉泉路1号”还是“蔡元培故居”，
他们都摇头说不知道；又去问植物园门口小卖部里的阿姨，一位阿姨说：“故居没听说过，
你要么往植物园公交站那里去看看，好像有两幢别墅洋房。
'''

#if __name__== '_main_':
en_result=stats_text_en(en_text)
cn_result=stats_text_cn(cn_text)
print('统计参数中每个英文单词出现的次数',en_result)
print('统计参数中每个中文汉字单词出现的次数',cn_result)

   
