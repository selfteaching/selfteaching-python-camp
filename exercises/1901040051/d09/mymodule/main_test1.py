import json
import sys
sys.path.append("c:")
import stats_word


# try:
#     stats_word.stats_text()
# except  ValueError:
#     print('Invalid argument.')

with open('tang300.json','r',encoding='UTF-8') as f:

    text = f.read()

    try:

        stats_text_cn(text)

    except ValueError as e:

        print("ERROR",e)