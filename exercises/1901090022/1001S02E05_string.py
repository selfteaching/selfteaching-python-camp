import re

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

# 1. 字符串的基本处理
# 1.2. 将字符串样本 text ⾥的 better 全部替换成 worse
print("===== 1.2. 将字符串样本 text ⾥的 better 全部替换成 worse =====")
text_replace_witch_worse = text.replace('better', 'worse')
print(text_replace_witch_worse)

# 1.3. 从第 2 步的结果⾥，将单词中包含 ea 的单词剔除
print("===== 1.3. 从第 2 步的结果⾥，将单词中包含 ea 的单词剔除 =====")
lines = text_replace_witch_worse.splitlines(True)
print(lines)

text_without_ea = ""
for row in lines:
    new_word_list = []
    for word in row.split(' '):
        new_word = re.sub(r'[a-zA-Z]*ea[a-zA-Z]*', "", word)
        new_word_list.append(new_word)
    text_without_ea += " ".join(new_word_list)
    
print(text_without_ea)

# 1.4. 将第 3 步的结果⾥的字⺟进⾏⼤⼩写翻转（将⼤写字⺟转成⼩写，⼩写字⺟转成⼤写）
print("===== 1.4. 将第 3 步的结果⾥的字⺟进⾏⼤⼩写翻转（将⼤写字⺟转成⼩写，⼩写字⺟转成⼤写） =====")
text_with_swapcase = text_without_ea.swapcase()
print(text_with_swapcase)

# 1.5 将第 4 步的结果⾥所有单词按 a…z 升序排列，并输出结果
print("===== 1.5 将第 4 步的结果⾥所有单词按 a…z 升序排列，并输出结果 =====")
word_list_without_sort = []
for row in text_with_swapcase.splitlines(True):
    for word in row.split(' '):
        match_obj = re.search('([a-zA-Z\']+)', word)
        if match_obj is not None:
            word_list_without_sort.append(match_obj.group(1))
        # print(match_obj)
        # print(word)
# word_list_sorted = sorted(word_list_without_sort)
word_list_without_sort.sort()
print(word_list_without_sort)
