text={'你':1,'好':2,'吗':3,'abc':4}

from mymodule import stats_word
try:
    stats_word.stats_text(text)
except:
    print('ERROR：text类型错误，请输入字符串文本。')