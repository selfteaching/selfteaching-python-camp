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
'''

def stats_text_en(text): #统计参数中每个英⽂单词出现的次数，最后返回⼀个按词频降序排列的数组
    text1=text.replace(',','').replace('.','').replace('--','').replace('*','').replace('!','')
    text2=text1.split()
    dict1={}
    for letter in text2:
        if letter in dict1:
            dict1[letter]=dict1[letter]+1
        else:
            dict1[letter]=1
    dict2=sorted(dict1.items(),key = lambda x:x[1],reverse = True)
    return dict2

print("统计参数中每个英⽂单词出现的次数，最后返回⼀个按词频降序排列的数组")
print(stats_text_en(text))

print()

text_cn='''
在没风的地方找太阳,在你冷的地方做暖阳,人事纷纷,你总太天真
'''
def stats_text_cn(text_cn): #统计参数中每个中⽂汉字出现的次数，最后返回⼀个按字频降序排列的数组
    text_cn1=text_cn.replace(',','')
    
    word_list=[]
    for character in text_cn1:
        if '\u4e00'<='\u9fa5':
            word_list.append(character)
    
    word_dict={}
    set1=set(word_list)
    for character in set1:
        word_dict[character]=word_list.count(character)

    word_dict1=sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    return word_dict1

print("统计参数中每个中⽂汉字出现的次数，最后返回一个按字频降序排列的数组")
print(text_cn)
print(stats_text_cn(text_cn))

