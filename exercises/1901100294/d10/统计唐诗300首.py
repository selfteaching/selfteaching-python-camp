import json
import collections
import jieba

tangshi_str_list = []

with open('tang300.json',encoding='utf_8') as f:
    read_data = f.read()
    tangshi_list = json.loads(read_data)
    #print(tangshi_list)
    for tangshi_dic in tangshi_list:
        #print(tangshi_dic)
        for value in tangshi_dic.values(): #提取 字典 里所有的 值
            #print(key,value)
            string = value
            tangshi_str_list.append(string)
#print(tangshi_str_list)

#把列表中所有 数字 变成 字符串
tangshi_str_list = [str(i) for i in tangshi_str_list] 

#把 list 转化成 str
tangshi_str = ''.join(tangshi_str_list) 

cn_characters = []

for character in tangshi_str:
    #unicode 中 中文 字符的范围
    if '\u4e00' <= character <= '\u9fff':
        cn_characters.append(character)

cn_str = ''.join(cn_characters)

seg_list = jieba.cut(cn_str,cut_all=False)
cn_str_done = "/".join(seg_list)
#print(cn_str_done)

cn_str_list = cn_str_done.split('/') #按照 / 切分成列表
#print(cn_str_list)

cn_list_filtered = list(filter(lambda s: s in cn_str_list and len(s) >= 2, cn_str_list)) #过滤后只保留大于等于2的词


cnt_cn = collections.Counter(cn_list_filtered).most_common(20)

print(cnt_cn)
