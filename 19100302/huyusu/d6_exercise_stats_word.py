text ='''
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

1. 将本地仓库关于本次作业的变更提交为一个commit
2. 通过Github桌面客户端将本地电脑的变更推送到自己账户下的作业仓库
3. 回到Github自己账户下的作业仓库页面，向远程公用作业仓库的master分支发起Pull
Request，在提交的 Pull Request的标题（ title）中填写自己的班级编号+作业编号，如
 示例： 19100101 day1 ，并在评论（comment ）中@自己的教练，提醒他检查作业

'''

a = text.lower()
a = a.split()  # 指定分隔符对字符串进行切片
a.pop()  # 删除list中的中文元素
found = {}  # 初始化一个词典


def stats_text_en():      # 定义检索中文函数
    """统计参数中每个英文单词出现的次数"""  # 注释
    global text  # 把text标记为全局变量
    for i in a:
        if i in found:
            found[i] += 1
        else:
            found[i] = 0
        found[i] += 1



    print('英文单词词频：', sorted(found.items(), key=lambda x: x[1], reverse=True))  # 词频降序


stats_text_en()    # 调用函数

# 统计中文词频


import re


def stats_text_cn():      # 定义检索英文函数
    """统计参数中每个中文单词出现的次数"""  # 注释
    global text  # 把text标记为全局变量
    found = {}      # 初始化一个词典

    # 提取中文字符串
    text = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", text)
    text = text.replace("  ", '')  # 提取的中文字符串会算上空格，会被统计上，故移除空格
    #print(text)                   #感觉多余

    for i in text:
        if i in found:
            found[i] += 1
        else:
            found[i] = 0
            found[i] += 1


    print('中文汉字字频： ', sorted(found.items(), key=lambda x: x[1], reverse=True))

stats_text_cn()   # 调用函数
