from collections import Counter
import jieba
import json
import re
with open("tang300.json","r",encoding="utf-8") as f:
    data=str(json.load(f))
    list_cn=re.findall(u'[\u4e00-\u9fa5]+',data)
    list_cn1=[]
    for x in list_cn:
        if len(x)>=2:
            list_cn1.append(x)
        else:
            continue
print(Counter(list_cn).most_common(20))