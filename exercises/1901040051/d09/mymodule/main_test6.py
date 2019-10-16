import re
import json
import sys
import collections
from collections import Counter
sys.path.append("c:")
import jiejian3
from jiejian3 import stats_text
text_en_cn = '''学习感觉进入到了正轨了,今天的学习还是蛮顺利的。I feel good in study，I feel it's fine today.'''
print(stats_text(text_en_cn,2))