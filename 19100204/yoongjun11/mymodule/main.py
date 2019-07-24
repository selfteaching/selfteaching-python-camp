try :
	import stats_word
except :
	print('stats_word.py模块不在当前目录,程序出错退出')
	exit()
import json
with open('tang300.json','r', encoding='utf-8') as f:
    temp = json.loads(f.read())


str = json.dumps(temp,ensure_ascii=False) 

int_num=20
print('词频文件tang300.json内容中词频前',int_num,' 的词和词频数为：')
print(stats_word.stats_text(str,int_num))

#10