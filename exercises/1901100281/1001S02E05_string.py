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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
text2 = text.replace( 'better', 'worse')
print('----将 better 全部替换成 worse----', text2)

text3 = text2.split()
for x in text3:
    if x.find('ea') != -1:
        delete = text3.index(x)
        del text3[delete]
        continue
print('----将包含 ea 的单词剔除----\n', text3)

texta = ' '.join(text3)
text4 = texta.swapcase()
print('----将字母进行大小写翻转----\n', text4)

text5 = text4.split()
print('----将所有单词按 a…z 升序排列----\n', sorted(text5))