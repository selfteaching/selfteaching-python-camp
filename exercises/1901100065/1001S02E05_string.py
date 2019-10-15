text = '''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
unless explicitly silenced.
In the face of ambxiguety, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- lets's do more of those!
'''

text_step2 = text.replace('better','worse') # 将text里的better全部替换成worse

text_list = text_step2.split() # 使用none作为分割符对第二步的文本进行拆分

text_list_step3 = [x.strip(',.-!*') for x in text_list if ((x.strip(',.-!*\'') != '') and ('ea' not in x.strip(',.-!*')))] # 对拆分后的列表内容进行整理，保留单词本身, 并剔除所有包含'ea'的单词

text_list_step4 = [x.swapcase() for x in text_list_step3] # 将第3步里的字母进行大小写翻转

text_list_step4.sort(key=str.lower) # 所有单词按a...z升序排列 
print(text_list_step4)              # 输出结果


