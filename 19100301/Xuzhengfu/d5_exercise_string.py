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


# 一、字符串的基本处理
# 1、创建一个名为 d5_exercise_string.py 的文件
# 2、将字符串样本text里的better全部替换成worse
text = text.replace('better','worse')

# 3、从第2步的结果里，将单词中包含ea的单词剔除
symbol_deleting = [',','.','!','-','*']  # 将非词类字符均替换为空格
for x in symbol_deleting:
   text = text.replace(x,'')

text_list = text.split()                 # 以空格为分隔符，分隔字符串text，使之成为列表text_list
character = "ea"
text = []                                # 创建空列表放置不含“ea”的单词
for i in text_list:
   if i.find(character) == -1:           # 找出不含”ea"的单词
      text.append(i)                     # 将它们添加至列表text

# 4、将第3步的结果里的字母进行大小写翻转（将大写字母转成小写，小写字母转成大写）
text_string = ' '.join(text)             # 将列表text转换为字符串
text_string = text_string.swapcase()     # 大小写翻转

# 5、将第4步的结果里所有单词按a...z升序排列，并输出结果
text_string = text_string.lower()        # 将已被大小写翻转的字符串 text_string 全部转换成“小写”，为求“正确排序”
text_list_final = text_string.split()    # 将全为小写的字符串 text_string 转换成列表 text_list_final
print(sorted(text_list_final))           # 升序排列