# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:46:48 2019

@author: PetalSaya
"""

import stats_word

with open('tang300.json','r',encoding = 'UTF-8') as file:
    load_dict = file.read()

try:
    stats_word.stats_text_cn(load_dict,20)
except ValueError:
    print ("Catch you, check the input type please!")
    