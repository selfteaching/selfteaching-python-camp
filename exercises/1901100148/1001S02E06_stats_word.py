# 1. 定义一个名为 stats_text_en 的函数，函数接受一个字符串 text 作为参数
# 函数元素有 函数名 参数 返回值 调用
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
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
def stats_text_en(text):    # 统计参数中英文单词出现的次数，最后返回一个按词频降序排列的数组（列表）
    # 分割文本为单词
    elements=text.split()
    # 定义一个空列表，用于存放过滤后的单词
    words=[]
    # 去掉非单词符号
    symbols='.,*-!'
    for element in elements:
        for symbol in symbols:
            element=element.replace(symbol,'')
        if len(element):#单词长度是否大于0，大于0则为单词，否则是空格
            words.append(element)

    # 初始化一个dict（字典）类型的变量，用来存放单词出现的次数
    counter={}
    word_set=set(words) #set集合里的元素是无序且不重复的。
    for word in word_set: # 遍历的时候也会减少遍历的次数
        counter[word]=words.count(word)
    # 函数返回值用 return 进行返回，如果没有 return 返回值则为 None。
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)   




# 2.定义stats_text_cn 函数，接受一个字符串作为参数，统计参数中每个汉字出现的次数，最后返回一个按字频降序排列的数组
cn_text='''现在每个我遇见的笑着的人，
他们都不曾因为苦而放弃，他们只因扛而成长。
谁不希望自己活得轻松，没有压力，一切随性，
但如果你真的那样去做的话，你会发现这个世界都在和你作对。
如果有一天你真的觉得自己轻松了，那也不是因为生活越来越容易了，
而是因为我们越来越坚强。'''

def stats_text_cn(text):
    cn_characters = [] # characters字符
    for character in text:
        # unicode 中 中文 字符的范围
        if'\u4e00'<=character<='\u9fff':
            cn_characters.append(character)
    counter={}
    cn_character_set=set(cn_characters) # 把中文字符列表转化成一个集合的形式，去除重复的字符
    for character in cn_character_set: # 遍历集合
        counter[character]=cn_characters.count(character)#统计中文列表里字符的次数，且赋值给字典对应的项，就是字符出现的次数
    return sorted(counter.items(),key=lambda x:x[1],reverse=True) #进行降序排序

#搜索__name__==__main__
#一般情况下在文件内 测试 代码的时候以下面的形式进行
if __name__=='__main__':
    en_result=stats_text_en(en_text)
    cn_result=stats_text_cn(cn_text)
    print('统计参数中每个英文单词出现的次数-->\n',en_result)
    print('统计参数中每个中文汉字出现的次数-->\n',cn_result)


