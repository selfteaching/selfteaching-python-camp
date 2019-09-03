from mymodule import stats_word
s_text='''
愚公移山
太行、王屋两座山，方圆七百里，高七八千丈，本来在冀州南边，黄河北岸的北边。 

Old Man Yu Gong and the Mountains 
Old man Yu Gong’s house had two big mountains in front of it.

'''
result=stats_word.stats_text(s_text)
print("统计结果\n",result)