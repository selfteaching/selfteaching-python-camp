from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

text = '''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
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
'''

txt_lower = text.lower()  # 统计某个单词出现的次数时不区分大小写，将字符串 text 里的字母全部转化成小写。
#print(f'将 text 里的字母全部转化成小写：', txt1)

# 将非英文字符用空格替换
txt = txt_lower.replace(',', '').replace('.', '').replace('--', '').replace('!', '').replace('*', '')
#print(f'去除非英文字符：', txt)

txt_list = txt.split() # 将字符串 txt 拆分成单个的单词，便于后续统计单词出现的次数
#print(f"拆分成单个的单词：", txt_list, sep='\n')

word_frequency_dict = {}    # 创建字典，dict也有去重的功能，所以可根据索引对list中的元素（单词）逐一统计
for i in range(len(txt_list)):
    word_frequency_dict.setdefault(txt_list[i], txt_list.count(txt_list[i]))
# print(f"统计字符串 text 中各个英⽂单词出现的次数：", word_frequency_dict, sep='\n')

# 按照单词出现的次数，从大到小排列。
# word_frequency_dict_items是一个list，它的元素是tuple，tuple的元素包含一个字符串和一个数字，('str', 8)
# word_frequency_dict.items()的结果是 dict_items(word_frequency_dict_items)
word_frequency_dict_items = sorted(word_frequency_dict.items(), key=lambda value:value[1], reverse=True)
# print(f'原始状态', word_frequency_dict.items(), sep='\n')
# print(f'从大到小排列', word_frequency_dict_items, sep='\n')

#for i in range(len(word_frequency_dict_items)):
#    print(word_frequency_dict_items[i])

print(f'按照单词出现的次数从⼤到⼩排列：')
for word,freq in word_frequency_dict_items:
    print(word, freq)