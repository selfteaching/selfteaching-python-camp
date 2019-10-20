from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'
import traceback
import json
from mymodule import stats_word

with open(r'H:\【自学Python】\GitHub\selfteaching-python-camp\exercises\1901010109\d09\tang300.json', 'rb') as f:
    text = f.read()
    text_str = text.decode( encoding='utf-8' )
    try:
        print( f"文件里出现次数前100的汉字，降序排列：" )
        for key,value in stats_word.stats_text_cn(text_str):
            print( key, value )
    except Exception as e:
        print( traceback.format_exc() )