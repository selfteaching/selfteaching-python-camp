text = 1213
from mymodule import stats_word 
import traceback
try:
    result = stats_word.stats_text(text )
    print ('最终的结果是==>',result)
except Exception as a:
    print('出现错误，错误类型为==>',a)
    print(traceback.format_exc())