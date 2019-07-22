# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 13:47:05 2019

@author: PetalSaya
"""

import operator
text = '''
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

Step1 = text.replace('.','').replace('--','.').replace('*','').replace('!','').lower()
Step2 = dict()
Step3 = Step1.split()
for word in Step3:
    if word in Step2:
        Step2[word] += 1
    else:
        Step2[word] = 1
Step4=sorted(Step2.items(),key=operator.itemgetter(1),reverse=True)
print (Step4)
