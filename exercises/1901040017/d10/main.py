

import re
	
from mymodule.stats_word import stats_text_cn

with open('d09/tang300.json', 'r', encoding='UTF-8') as poem:
    read_file = poem.read()
poem.closed
	
print('最多的20个词：', stats_text_cn(read_file, 20))


  







