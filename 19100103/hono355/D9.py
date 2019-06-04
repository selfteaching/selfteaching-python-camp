import json
with open('E:\\tang300.json') as f:
    file1 = f.read()
print('top100 => ', stats_word.stats_text_cn(file1,100)) 
#调用stats_word模块中的stats_text_cn函数