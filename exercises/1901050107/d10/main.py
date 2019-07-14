
#<<<<<<< master
# encoding=utf-8
import jieba
import path
from mymodule import stats_word

path_str = "/Users/mac/Desktop/selfteaching-python-camp/exercises/1901050107/d10/tang300.json"
with open(path_str,'r') as tangshi:
    data =  tangshi.read()  

print(stats_word.stats_text_cn(data,20))

# # 恢复字符串格式
# chars = ''.join(chars)        
# seg_list = jieba.cut(chars,cut_all=False) #精确模式
# segb.join(seg_list).split(',')
# chars = []
# # 排除长度小于2的词语
# for item in seg_str:
#     if len(item) > 1:
#         chars.append(item)
# print(Counter(chars).most_common(20))
#=======
import jieba
from collections import Counter
path = "exercises/1901050107/d10/tang300.json"
with open(path) as tangshi:
    data = tangshi.read()   
chars = []
# 排除字符串里面的非汉字字符
for item in data:
    if '\u4e00' <= item <= '\u9fff':
        chars.append(item)
# 恢复字符串格式
chars = ''.join(chars)        
seg_list = jieba.cut(chars,cut_all=False) #精确模式
seg_str = ','.join(seg_list).split(',')
chars = []
# 排除长度小于2的词语
for item in seg_str:
    if len(item) > 1:
        chars.append(item)
print(Counter(chars).most_common(20))
#>>>>>>> master

