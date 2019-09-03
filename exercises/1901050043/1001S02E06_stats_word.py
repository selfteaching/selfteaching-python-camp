string1 ='''
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
鹅鹅鹅，曲项向天歌，白毛浮绿水，红掌拨清波。'''
import re

def stats_text_en(text):
    '''This function aims to count English words.'''
    
    result = re.sub("[^A-Za-z]", " ", text.strip())
    newList = result.split()
    a ={}
    for i in newList:
        a.update({i:newList.count(i)})
    a1= sorted(a.items(), key= lambda x:x[1],reverse = True)
    print('the result of counting english words： ',a1,'\n')

def stats_text_cn(text):
    ''' This function aims to count Chinese words.'''
    
    result1 = re.findall(u'[\u4e00-\u9fff]', text)
    newString = result1
    b ={}
    for i in result1:
        b.update({i:newString.count(i)})
    b1 = sorted(b.items(),key = lambda x:x[1],reverse= True)
    print('the result of counting chinese words ', b1, '\n')
    
stats_text_en(string1)
stats_text_cn(string1)