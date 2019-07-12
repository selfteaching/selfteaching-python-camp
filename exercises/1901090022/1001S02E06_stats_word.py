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

"""
统计参数中每个英⽂单词出现的次数;
最后返回⼀个按词频降序排列的数组
"""
def stats_text_en(text):
    word_dict = {}
    for word in text.split():
        match_obj = re.search('([a-zA-Z]+)', word)
        if match_obj is not None:
            w = match_obj.group(1).lower()
            if w in word_dict:
                word_dict[w] += 1
            else:
                word_dict[w] = 1

    # 参考：https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
    return sorted(word_dict.items(), key=lambda item: item[1], reverse=True)
word_count = stats_text_en(text)
print(word_count)

def stats_text_cn(text):
    word_dict = {}
    # for word in text.split(''):
    for word in text:
        if '\u4e00' <= word <= '\u9fff':
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    return sorted(word_dict.items(), key=lambda item: item[1], reverse=True)

text_cn = '''
1. 将本地仓库关于本次作业的变更提交为一个 commit

2. 通过 Github 桌面客户端将本地电脑的变更推送到自己账户下的作业仓库

3. 回到 Github 自己账户下的作业仓库页面，向远程公用作业仓库的 master 分支发起 Pull Request，在提交的 Pull Request 的标题（title）中填写自己所在的钉钉群名，如示例： 【032901】自学训练营 DAY1 ，并在评论（comment）中 @自己的助教（请向助教索要他的 Github 用户名）提醒他检查作业
'''
word_count_cn = stats_text_cn(text_cn)
print(word_count_cn)