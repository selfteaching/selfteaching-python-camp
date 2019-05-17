# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:46:48 2019
@author: PetalSaya
test by jiangzhenye 20190509
"""

import stats_word
import json

with open('tang300.json','r',encoding = 'UTF-8') as file:
    load_dict = file.read()

try:
    stats_word.stats_text_cn(load_dict,20)
except ValueError:
    print ("Catch you, the input type should be string! Check it please!")