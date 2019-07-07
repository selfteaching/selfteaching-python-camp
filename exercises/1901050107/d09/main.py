
path = "exercises/1901050107/d09/tang300.json"
import os
from mymodule import stats_word
with open(path) as f:
    data = f.read()
 
from collections import Counter
chars = []
cnt = Counter()
for item in data:
    if '\u4e00' <= item <= '\u9fff':
        chars.append(item)
print(Counter(chars).most_common(100))   
