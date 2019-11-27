text_sample = '''
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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

#将字符串串样本 text ⾥里里的 better 全部替换成 worse
text = text_sample.replace('better','worse')
print(text)

#从第 2 步的结果⾥里里，将单词中包含 ea 的单词剔除
words = text.split()
notea = []
for word in words:
    if word.find('ea') < 0:
        notea.append(word)
print(notea)

#将第 3 步的结果⾥里里的字⺟母进⾏行行⼤大⼩小写翻转
daxiao = [i.swapcase() for i in notea]
print(daxiao)

#将第 4 步的结果⾥里里所有单词按 a…z 升序排列列，并输出结果
shenxu = sorted(daxiao)
print(shenxu)