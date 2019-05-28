# today's tasks used the same one parameter "text" 
# (a variable should be assigned with strings including both en and cn)
text = '''
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

真, 有改天换地的伟力. by 核聚 @ wechat id: hejupai
...循序渐进虽然难受, 但它能够有效避免思维混乱, 也因此, 循序渐进就是学习的捷径...
...最后, 最重要的是, 你是真的在学习.
真, 太难了.
只一日之间, 你已经联想到'衣带渐宽终不悔,为伊消得人憔悴'.
那么, 两日三日, 乃至日以继夜数十年, 那会有多少难?
真, 太难.
但, 真, 有改天换地的伟力.
在人的精神世界里, 真, 能改变一切, 造就一切.
祝, 开心.
祝, 勇猛精进.
'''

# Task1 
import re # call out regular expressions module when dealing with cn? 

# let define this function (its name is stats_text_en)
def stats(originObj, newDict) :
    d = newDict
    for m in originObj :
        d[m] = d.get(m, 0) + 1 # used the get function?
    return d


def stats_text_en(text_en):
    '''
    # TODO
    '''
    # dealing with chinese strings(non a-zA-Z dead)
    result_en = re.sub("[^A-Za-z]", " ", text_en.strip())

    list1 = result_en.split() # let's change the strings into a list
    # import collections
    
    # return collections.Counter(list1)
    words = dict()
    stats(list1, words)
    newWords = sorted(words.items(), key=lambda item: item[1], reverse=True) 
    return dict(newWords)# if no "return" it wont run here, but it's ok in original code 




# Task2
# copied from @echojce and revised with some of my thoughts
# not clarified and required further digging 
# with my thoughts and comments and questions 
def stats_text_cn(text_cn): 
    #FIXME @echojce thoughts: 
    ''' 统计中文汉字字频
    
    第一步：过滤汉字字符，并定义频率统计函数 stats()。\n
    第二步：清除文本中的标点字符,将非标点字符组成新列表 new_list。\n
    第三步：遍历列表，将字符同上一次循环中频率统计结果作为形参传给统计函数stats()。\n
    第四步：统计函数在上一次统计结果基础上得出本次统计结果，赋值给newDict。\n
    第五步：new_list遍历结束，输出倒序排列的统计结果。\n
    '''
    result_cn = re.findall(u'[\u4e00-\u9fff]+', text_cn)
    str2 = ''.join(result_cn)



    words = dict()
    stats(str2, words)

    newWords = sorted(words.items(), key=lambda item: item[1], reverse=True) 
    return dict(newWords)# if no "return" it wont run here, but it's ok in original code 

# y = stats_text_cn(text)
# print(y) 
# I used "stats_text_cn(text)"to call the function ,,,it worked here...sign .but why not en one?..

# call those two function
result_cn = stats_text_cn(text)
print('中文汉字字频统计结果： ', result_cn)# if no "return" it wont run here, but it's ok in original code 

result_en = stats_text_en(text)
print('英文汉字字频统计结果： ', result_en)# if no "return" it wont run here, but it's ok in original code 