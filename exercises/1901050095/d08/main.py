from mymodule import stats_word  as counts      #模块导入mymodule目录下的stats_word.py文件
text = 1234567890	 # 把一个数字（非字符串）赋值给变量text
try:	#用 try...except 触发异常并执行
	counts.stats_text(text)
except ValueError:
	print("您所输入的非字符串。请重新输入：")