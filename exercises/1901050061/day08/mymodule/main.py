# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:46:48 2019
@author: PetalSaya
test by jiangzhenye 20190509
"""

import stats_word
text = 22222333333111111
#text = "hello"
#text = "hello hello hello hello"
#text = "你好"

try:
    stats_word.stats_text(text)
except ValueError:
    print ("Catch you, the input type should be string! Check it please!")