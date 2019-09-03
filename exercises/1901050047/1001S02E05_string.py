# 1.将better全部替换成worse
# 2.将字符串样本text里英文单词中包含ea的英文单词剔除
# 3.大写字母转成小写，小写字母转成大写
# 4.将所有单词按a...z升序排列
# 5.最后输出结果

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
x = 'better'
print(f'{x}出现了{text.count(x)}次')    # 计算'better'出现几次
text1 = text.replace('better', 'worse')  # 用‘worse‘全部替换’better‘
y = 'worse'
print(f'{y}出现了{text1.count(y)}次')  # 计算'worse'出现几次

text2 = text1.replace(',',' ').replace('.',' ').replace('--',' ').replace('*',' ').replace('!',' ')   
# 将非英文字符替换为空格

list_text = text2.split()   # 以空格，把字符串内单词拆分为列表

my_list = []   # 新建一个列表，用于存放新的内容
for i in list_text :   # 循环遍历列表list_text
    if i.find('ea') == -1 :  # sub 未被找到'ea'则返回 -1
        my_list.append(i)   #  把单词添加到序列的末尾
print(my_list)  # 打印不含有'ea‘单词的新列表 

my_list1 = []  # 新建一个列表，用于存放新的内容
for i in my_list :   # 循环遍历列表中的单词
    x = i.swapcase()    # 单词的大小写转换
    my_list1.append(x)  # 逐个拷贝到新的列表中
print(my_list1)    

my_list1.sort()  # 将所有单词按a...z的升序排列
print(my_list1)