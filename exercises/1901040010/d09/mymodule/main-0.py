text = '''
This is a wonderful day. It is a sunny hot day.
昨天下雨了，今天又下雨了，明天还会下雨吗？
'''

from stats_word import stats_text

try:
    stats_text(text,5)
except ValueError:
    print('The text should be a string.')