import re
from collections import Counter

text = '''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

re --- 正则表达式操作

模式和被搜索的字符串既可以是 Unicode 字符串 (str) ，也可以是8位字节串 (bytes)。 但是，Unicode 字符串与8位字节串不能混用：也就是说，你不能用一个字节串模式去匹配 Unicode 字符串，反之亦然；类似地，当进行替换操作时，替换字符串的类型也必须与所用的模式和搜索字符串的类型一致。
正则表达式使用反斜杠（'\'）来表示特殊形式，或者把特殊字符转义成普通字符。 而反斜杠在普通的 Python 字符串里也有相同的作用，所以就产生了冲突。比如说，要匹配一个字面上的反斜杠，正则表达式模式不得不写成 '\\\\'，因为正则表达式里匹配一个反斜杠必须是 \\ ，而每个反斜杠在普通的 Python 字符串里都要写成 \\ 。
解决办法是对于正则表达式样式使用 Python 的原始字符串表示法；在带有 'r' 前缀的字符串字面值中，反斜杠不必做任何特殊处理。 因此 r"\n" 表示包含 '\' 和 'n' 两个字符的字符串，而 "\n" 则表示只包含一个换行符的字符串。 样式在 Python 代码中通常都会使用这种原始字符串表示法来表示。
绝大部分正则表达式操作都提供为模块函数和方法，在 编译正则表达式. 这些函数是一个捷径，不需要先编译一个正则对象，但是损失了一些优化参数。
'''

# 统计英文
def stats_text_en(text,count):
	
	# 判断text是否为字符串类型
	if isinstance(text,str) != True:
		raise ValueError('Invalid args:',text,'it is not string.')
	
	# 匹配英文
	word_list = re.findall(r'\b[a-z]+\'?[a-z]+',text.lower())

	# 统计英文词频
	cnt = Counter(word_list)
	return(cnt.most_common(count))

# 统计中文
def stats_text_cn(text,count):

	# 判断text是否为字符串类型
	if isinstance(text,str) != True:
		raise ValueError('Invalid args:',text,'it is not string.')	
	
	# 删除text中的英文、标点、数字
	text_cn = re.sub(r'[\Wa-zA-Z0-9]','',text)

	# 统计中文词频
	cnt = Counter(text_cn)
	return(cnt.most_common(count))

def stats_text(text,count):

	# 判断text是否为字符串类型
	if isinstance(text,str) != True:
		raise ValueError('Invalid args:',text,'it is not string.')

	# 对text分别调用统计中文和英文的函数
	list_en = stats_text_en(text,count)

	list_cn = stats_text_cn(text,count)

	# 合并list_en和list_cn，重新排序
	list_all = sorted((list_en + list_cn), key = lambda x: x[1], reverse=True)

	return list_all

#print(stats_text(text,20))