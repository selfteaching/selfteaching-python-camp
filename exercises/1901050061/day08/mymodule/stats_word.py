# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 16:58:18 2019
@author: PetalSaya
test by jiangzhenye 20190509
"""

import operator
import re

def stats_text_en(text):
    if type(text) != str:
        raise ValueError("Input needs to be a string.")
    Step1 = re.sub("[\u4e00-\u9fa5，。：？！「」、]","",text.strip())
    #Step1 deletes the non-word character
    Step2 = dict()   #Step2 creates the empty dictionary 
    Step3 = Step1.split()   #Step3 splits each word in text into a single unit 
    for word in Step3:   #for...in loop counts the unit and records into the dictionary
        if word in Step2:
            Step2[word] += 1  
        else:
            Step2[word] = 1   #New word counts for one
    Step4 = sorted(Step2.items(),key=operator.itemgetter(1),reverse=False)
    # operator modulate helps rank the # of times of each word appealed in the text
    print (Step4)   # Print result


def stats_text_cn(text):
    if type(text) != str:
        raise ValueError("Input needs to be a string.")
    Step1 = ''.join(re.findall(u'[\u4e00-\u9fa5]+',text))
    Step2 = dict()   #Step2 creates the empty dictionary 
    Step3 = range(len(Step1))  #Step3 gives each cn word a position # 
    for word in Step3:   #for...in loop counts the cn word and records into the dictionary
        if Step2.get(Step1[word]):   #get() the cn word from each position #  
            Step2[Step1[word]] += 1  
        else:
            Step2[Step1[word]] = 1   #New cn word counts for one
    Step4 = sorted(Step2.items(),key=operator.itemgetter(1),reverse=False)
    # operator modulate helps rank the # of times of each cn word appealed in the text
    print (Step4)   # Print result

def stats_text(text):
    if type(text) != str:
        raise ValueError("Input needs to be a string.")
    stats_text_en(text)
    stats_text_cn(text)