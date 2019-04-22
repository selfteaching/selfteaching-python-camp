# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 16:58:18 2019

@author: PetalSaya
"""

import operator
import re

def stats_text_en(text):
    Step1 = text.replace(',','').replace('.','').replace('--','.').replace('*','').replace('!','').lower()
    #Step1 deletes the non-word character
    Step2 = dict()   #Step2 creates the empty dictionary 
    Step3 = Step1.split()   #Step3 splits each word in text into a single unit 
    for word in Step3:   #for...in loop counts the unit and records into the dictionary
        if word in Step2:
            Step2[word] += 1  
        else:
            Step2[word] = 1   #New word counts for one
    Step4=sorted(Step2.items(),key=operator.itemgetter(1),reverse=False)
    # operator modulate helps rank the # of times of each word appealed in the text
    print (Step4)   # Print result


def stats_text_cn(text):
    Step1 = ''.join(re.findall(u'[\u4e00-\u9fa5]+',text))
    Step2 = dict()   #Step2 creates the empty dictionary 
    Step3 = range(len(Step1))  #Step3 gives each cn word a position # 
    for word in Step3:   #for...in loop counts the cn word and records into the dictionary
        if Step2.get(Step1[word]):   #get() the cn word from each position #  
            Step2[Step1[word]] += 1  
        else:
            Step2[Step1[word]] = 1   #New cn word counts for one
    Step4=sorted(Step2.items(),key=operator.itemgetter(1),reverse=False)
    # operator modulate helps rank the # of times of each cn word appealed in the text
    print (Step4)   # Print result

text1 = '''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.Special cases aren't special enough to break the rules.
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
stats_text_en(text1)

text2 = '''
糖果的小楠姐姐是无比的漂亮，
白哥和小温辅导是无比的帅气，
要多加几个无比才能显现出统计的意义，
那就今天是个无比开心(*^▽^*)的一天!
'''
stats_text_cn(text2)

  