# 第10天作业2
# 2019年3月30日
# 完善词频统计的排序功能主程序
# 通过导入模块stats_word,调用stats_text,
# 下载唐诗300首文件tang300.json,存到main.py的同级文件夹下
# 读取文件中的内容
# 统计文件内容中汉字的词频，生成词频最高的前100个词


# 调用stats_word模块
# 在调用stats_word的地方采用try……except 捕抓异常
try :
	import stats_word
except :
	print('stats_word.py模块不在当前目录,程序出错退出')
	exit()

#读唐诗300首文件tang300.json，处理汉字格式
import json
with open('tang300.json','r', encoding='utf-8') as f:
    temp = json.loads(f.read())

#将json格式转为字符串，注意编码问题
str = json.dumps(temp,ensure_ascii=False) 




#print('统计唐诗300首文件内容中汉字的词频，词频最高的前100个汉字是： \n')

#调用stats_word模块中的stats_text函数，统计词频
# int _num词频统计数
int_num=20
print('词频文件tang300.json内容中词频前',int_num,' 的词和词频数为：')
print(stats_word.stats_text(str,int_num))


