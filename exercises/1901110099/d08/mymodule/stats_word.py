

def stats_text_en(text): #统计参数中每个英⽂单词出现的次数，最后返回⼀个按词频降序排列的数组
    
    if not isinstance(text,str): #添加参数类型检查，如果输入参数不为字符串类型则抛出 ValueError 错误，并包含完整的错误提示信息
        raise ValueError('参数必须是str类型，输入类型%s' % type(text))
    
    elements=text.split()
    words=[]
    symbols=',.*-!'
    for element in elements:
        for symbol in symbols:
            element=element.replace(symbol,'')
        if len(element) and element.isascii():
            words.append(element)

    counter={}
    word_set=set(words)

    for word in word_set:
        counter[word]=words.count(word)    
    
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)

    

def stats_text_cn(text): #统计参数中每个中⽂汉字出现的次数，最后返回⼀个按字频降序排列的数组
    
    if not isinstance(text,str): #添加参数类型检查，如果输入参数不为字符串类型则抛出 ValueError 错误，并包含完整的错误提示信息
        raise ValueError('参数必须是str类型，输入类型%s' % type(text))
    
    word_list=[]
    for character in text:
        if '\u4e00'<= character <= '\u9fff':
            word_list.append(character)
    
    word_dict={}
    set1=set(word_list)
    for wording in set1:
        word_dict[wording]=word_list.count(wording)

    word_dict1=sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    return word_dict1



def stats_text(text): #分别调⽤stats_text_en , stats_text_cn ，输出合并词频统计结果
    
    if not isinstance(text,str): #添加参数类型检查，如果输入参数不为字符串类型则抛出 ValueError 错误，并包含完整的错误提示信息
        raise ValueError('参数必须是str类型，输入类型%s' % type(text))
    
    return stats_text_cn(text)+stats_text_en(text)


if __name__ == "__main__":
    text='''
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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
在没风的地方找太阳，在你冷的地方做暖阳，人事纷纷，你总太天真
'''