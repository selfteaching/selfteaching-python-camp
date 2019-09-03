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
#2、将字符串样本text里的better全部替换成worse
new_string1 = text.replace("better", "worse")
print(new_string1)

# 3、从第2步的结果，将单词中包含的ea的单词剔除
'''
思路：
    1、先将text拆分成每个单词
        1）先把text拆成每一行
        2）再把每一行拆成每一个单词
    2、再判断每个单词中是否含有“ea"子字符串，如果有，则删除
    3、然后将每个单词合成代表一行的整字符串
    4、最后将每一行的字符串合成代表一个整字符串。
'''
line_list = []
for line in new_string1.split(sep=("\n")):
    word_list = line.split(" ")
    for word in word_list[:]:
        if "ea" in word:
            word_list.remove(word)
    line_list.append(' '.join(word_list))

new_string2 = '\n'.join(line_list)
print(new_string2)


# 4、将第3步的结果里的字母进行大小写翻转 （将大写字母转成小写，小写字母转成大写）
new_string3 = new_string2.swapcase()
print(new_string3)


# 5、將第4步的結果里所有的单词单词按a...z升序排序，并输出结果。
'''
1、把影响排序的单词，例如：--和*开头的单词做了替换
'''
word_lists = new_string3.replace("--",'').replace("*",'').replace("\n",' ').split(" ")
for word in word_lists[:]:
    if word == '':
        word_lists.remove(word)
#排序后的结果是一个列表
print(sorted(word_lists))
#排序后的结果是一个字符串
print(' '.join(sorted(word_lists)))


