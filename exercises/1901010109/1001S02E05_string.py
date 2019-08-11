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
# 将字符串样本 text ⾥的 better 全部替换成 worse
text_btw = text.replace('better', 'worse')
#print("将字符串样本 text ⾥的 better 全部替换成 worse 后：", text_btw)

# 将 text_btw 的单词中包含 ea 的单词剔除
text_del = text_btw.split() # 根据空格将字体串 text_btw 拆分成单个的单词
                        # 同时变成 list 类型，从而可以进行后续的删除和排序操作
#print(text_del)
for index, word in enumerate(text_del):
    if 'ea' in word:
        del text_del[index]
#print("将包含 ea 的单词全部剔除后：", text_del)

# 将 text_del ⾥的字⺟进⾏⼤⼩写翻转（将⼤写字⺟转成⼩写，⼩写字⺟转成⼤写）
for index, word in enumerate(text_del):
    text_del[index] = text_del[index].swapcase()
text_swap = text_del
#print("字⺟⼤⼩写翻转后：", text_swap)

# 将 text_swap ⾥所有单词按 a…z 升序排列，并输出结果
text_swap.sort()
print("所有单词按 a…z 升序排列：", text_swap)