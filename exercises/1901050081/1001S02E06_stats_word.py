#统计参数中每个英文单词出现的次数
def stats_text_en(text):
    elements=text.split()
    words=[]
    symbols=',.*-?!'
    for element in elements:
        for symbol in symbols:
            element=element.replace(symbol,'')
        if len(element):
            words.append(element)
    counter={}
    word_set=set(words)

    for word in word_set:
        counter[word]=words.count(word)
    return sorted(counter.items(), key=lambda x:x[1], reverse=True)

#统计参数中每个中文汉字出现的次数
def stats_text_cn(text):
    cn_charactors=[]
    for charactor in text:
        if '\u4e00' <= charactor <= '\u9fff':
            cn_charactors.append(charactor)
    counter={}
    cn_charactor_set=set(cn_charactors)
    for charactor in cn_charactor_set:
        counter[charactor]=cn_charactors.count(charactor)
    return sorted(counter.items(), key=lambda x:x[1], reverse=True)

en_text='''
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

cn_text='''
幸福一日
海子
我无限的热爱着新的一日
今天的太阳 今天的马 今天的花楸树
使我健康 富足 拥有一生
从黎明到黄昏
阳光充足
胜过一切过去的诗
幸福找到我
幸福说瞧 这个诗人
他比我本人还要幸福
在劈开了我的秋天
在劈开了我的骨头的秋天
我爱你花楸树
'''



if __name__ == '__main__':
    en_result=stats_text_en(en_text)
    cn_result=stats_text_cn(cn_text)
    print('统计参数中每个英文单词出现的次数:\n',en_result)
    print('统计参数中每个中文汉字出现的次数:\n',cn_result)