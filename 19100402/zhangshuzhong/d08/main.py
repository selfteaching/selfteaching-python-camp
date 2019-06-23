txt =[1,2.3,5,6,9]
from mymodule import stats_word
try:
    stats_word.stats_text(txt)
except ValueError as err:
    print('具体原因为:{0}'.format(err))#将错误的信息显示出来