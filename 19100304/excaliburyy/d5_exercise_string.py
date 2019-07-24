# 19100304 day5 银零
#【字符串的基本处理】
# 1.将字符串样本text里的better全部替换成worse
# 2.从第二步的结果里，将单词中包含ea的单词剔除
# 3.将第三步的结果里的字母进行大小写翻转
# 4.将第四步的结果里所有的单词按a...z升序排列
# 5.输出结果


# 原始文本
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

# 1.将字符串样本text里的better全部替换成worse
txt1 = text.replace('better','worse')

# 2.从第二步的结果里，将单词中包含ea的单词剔除
import re
list1 = re.split(r'(\W+)',text)     #将text字符串（string）转换为列表（list）,每一个单词和其他字符（空格，换行，‘.’，‘,’，‘*’），都成为list1列表中的一个元素
for i in list1:                     #当i属于list1列表当中的元素时，开始循环
    if 'ea' in i:                   #判断当'ea'属于i时，执行语句
        list1.remove(i)             #列表list1移除i  
txt2 = ''.join(list1)

# 3.将第三步的结果里的字母进行大小写翻转
txt3 = txt2.swapcase()

# 4.将第四步的结果里所有的单词按a...z升序排列
import re
list2 = re.split(r'\W+',txt3)       #将text3字符串（string）转换为列表list2,只保留单词为list2中的元素
list2.sort()
while '' in list2:                  #删除list2中为空的列表元素
    list2.remove('')

# 5.输出结果
txt4 = ' '.join(list2)
print(txt4)