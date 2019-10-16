# import sys
# sys.path.append('C:')

# import json

# with open('tang300.json', 'r') as f:
#     data = json.load(f)

# import json

# with open('C:\Users\Thinkpad\Documents\GitHub\selfteaching-python-camp\exercises\1901040051\d09\mymodule\tang300.json', 'r', encoding='utf-8') as f:
#     for line in f:
#         d = json.loads(line)
#         y = d['year']
#         print(y)

import json

with open('mymodule/tang300.json', encoding='utf-8') as f:
    # print(f)
    # line = f.readline()
    # # d = json.loads(line)
    # print(type(line))    
    # f.close()
    

    try:
        while True:
            line = f.readline()
            if line:
                r = json.loads(line)
                # print(type(r))
            else:
                break
    except:
        f.close()


import sys
sys.path.append('C:')
import stats_word
try:
    stats_word.stats_text(r)
except  ValueError:
    print('Invalid argument.')


