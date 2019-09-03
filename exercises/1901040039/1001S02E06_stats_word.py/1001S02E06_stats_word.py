def stats_text_en(text,symbols):
    text = text.strip().split()
    words = [] # for store the text after processing
    for word in text:
        for  symbol in symbols:
            word = word.replace(symbol,'') # delet the redundant symbols in the text
        words.append(word)

    word_set = set(words) # transfer the list to the set
    counter_dict = {}

    for word in word_set: # count the number for each word
        counter_dict[word] = words.count(word)
    aa = sorted(counter_dict.items(),key = lambda x: x[1], reverse = True)

    return print('the sorted word frequencies for the input english text',aa)

text_sample = '''
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
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
symbols = '.,*-!'

# a example calling the function english text 
stats_text_en(text_sample,symbols)



# 2 for chinese word
def stats_text_cn(text,symbols):
    text = text.strip().split()
    words = [] # for store the text after processing
    for word in text:
        for  symbol in symbols:
            word = word.replace(symbol,'') # delet the redundant symbols in the text
        words.append(word)

    words_cn = [] # for storing the chinese single character
    for word in words:
        for _i in word:
            words_cn.append(_i)
    # print(words_cn)
    word_set = set(words_cn) # transfer the list to the set

    counter_dict = {}

    for word in word_set: # count the number for each word
        counter_dict[word] = words_cn.count(word) # for a dict{key,value} this is: dict[key] = value (value is the frequencies for the word)
    aa = sorted(counter_dict.items(),key = lambda x: x[1], reverse = True)

    return print('the sorted word frequencies for the input chinese text',aa)

text_sample1 = '''
垃圾问题解决不好，群众不答应。垃圾分类，
是生产生活发展到一定阶段之后的产物，
是社会文明水平的重要体现。培养垃圾分类意识，
养成垃圾分类习惯，可以促进群众逐步形成绿色生活方式。
而不管是垃圾分类投放还是收集、转运、处理各个环节，
都需要资金投入，必须有相应的经济社会发展基础。
'''
symbols1 = '.,*-!。，/、？'

# a example calling the function chinese text
stats_text_cn(text_sample1,symbols1)