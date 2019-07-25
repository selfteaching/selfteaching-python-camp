import re
import json
import sys
import collections
from collections import Counter
sys.path.append("c:")
import stats_word

with open("mymodule/tang300.json", "r", encoding="utf-8") as file:
    try:
        read_data = file.read()         
        read_data = re.sub("[^\u4e00-\u9fff]+", "", read_data.strip())
        word_counts = Counter(read_data)
        word_counts_top = word_counts.most_common(100)
        print(word_counts_top)
    except ValueError as e:
        print(e)
