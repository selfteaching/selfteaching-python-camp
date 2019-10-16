text = '''
This is a wonderful day. It is a sunny hot day.
昨天下雨了，今天又下雨了，明天还会下雨吗？
'''

#<<<<<<< master
from stats_word import stats_text

print(stats_text(text))
#=======
import stats_word

stats_word.stats_text(text)
#>>>>>>> master
