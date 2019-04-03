
import os
import sys
sys.path.append("/Users/zhangdequan/Documents/GitHub/selfteaching-python-camp/19100302/DequanZhang/mymodule")
from stats_word import stats_text_cn

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tang300.json'))  as f:
    read_data = f.read()

print('词频统计Top20',stats_text_cn(read_data,20))