sample_text='''
The Zen of Python,by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren`t special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity,refuse the temptation tu guess.
There should be one--and preferably only one--obvious way to do it.
Although that way may not be obvious at fitst unless you`re Dutch.
NOw is better than never.
Although never is often bettet than*right*now.
If zhe implementation is hard to explan,it`s a bad idea.
If zhe implementation is easy to explan,it may be a good idea.
Namesoaces are one honking great idea--let`s do more of those!
'''

text=sample_text.replace('better','worse')
print('将better替换成worse=====',text)

words=text.split()
filtered=[]
for word in words:
    if word.find('ea')<0:
        filtered.append(word)
        
print('提出包含ea的单词=====',filtered)

swapcased=[i.swapcase() for i in filtered]
print('大小写反转======',swapcased)

print('a-z升序=====',sorted(swapcased))