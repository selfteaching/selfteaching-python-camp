from collections import Counter
import json
import jieba


with open("tang300.json", 'r', encoding='utf-8') as file_object:
    tang300_dict = json.load(file_object)
    #print(tang300_dict)

    tang300_str = ''
    for temp_dict in tang300_dict:
        tang300_str += temp_dict['contents']
        tang300_str += temp_dict['type']
        tang300_str += temp_dict['author']
        tang300_str += temp_dict['title']
    #print(tang300_str)
    seg_list = jieba.cut(tang300_str, cut_all=True)

    
    c = Counter()
    for seg in seg_list:
        if len(seg) > 1:
            c[seg] = c[seg] + 1
    print(c.most_common(20))


