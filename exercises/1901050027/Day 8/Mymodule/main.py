# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:46:48 2019

@author: PetalSaya
"""

import stats_word
text= 737611111810189111117

try:
    stats_word.stats_text(text)
except ValueError:
    print ("Catch you, check the input type please!")