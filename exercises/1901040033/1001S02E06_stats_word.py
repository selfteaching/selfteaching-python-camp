text = '''I believe, for every drop of rain
that falls, A flower grows.
I believe that somewhere in the
darkest night, A candle glows.'''

text = text.replace(',','').replace('.','').replace('!','').replace('*','').replace('--','')
text1 = text.split()

d = {}
for i in text1:
    if  i in d:
        d[i] += 1
    else: d[i] = 1
d=sorted(d.items(),key=lambda x:x[1],reverse=True) 
print(d)

import jieba
text_cn = '''我相信，每个雨滴飘落
就有一朵花儿生长.
我相信，即使最漆黑的夜晚
也会有蜡烛发出明亮的光'''

dele = {'。','！','？','的','“','”','（','）',' ','》','《','，'}
words = list(jieba.cut(text_cn))
articleDict = {}
articleSet = set(words)-dele
for w in articleSet:
    if len(w)>1:
        articleDict[w] = words.count(w)

articlelist = sorted(articleDict.items(),key = lambda x:x[1], reverse = True)

for i in range(10):
    print(articlelist[i])
	
