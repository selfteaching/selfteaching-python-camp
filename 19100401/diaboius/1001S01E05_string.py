#把vscode 安装到鼠标右键；
#把vscode中文化；
#配合vscode 的Python的运行环境；Pyton环境选择器并未出现；
text = '''
The Zen of python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases arent't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced
In the face of ambxiguity,refuse the temptation to guess
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch
If the implementation is hard to explain,it's a bad idea
If the implementation is easy to explain,it's may be a good idea.
Namespaces are one honking great idea --let's do more of those!
'''
print('****************************************\n第一步：better替换成worse:\n****************************************')
text=text.replace('better','worse')
print(text)


print('****************************************\n第二步：将字符串样本text里英文单词中包含ea的英文单词剔除:\n****************************************')
new_list_1 = text.split()
str1="ea"
str2=[]
for i in new_list_1:
    if i.find(str1) < 0:
        str2.append(i)
print(str2)

print('****************************************\n第三步：大小写字母转换:\n****************************************')
text=text.swapcase()
print(text)

print('****************************************\n第四步：将所有单词按a，...z升序排列:\n****************************************')
new_list_2=text.split()
new_list_2.sort()
print(new_list_2)
