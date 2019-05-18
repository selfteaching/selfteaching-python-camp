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


#better全部替换成worse
text = text.replace('better','worse')

#将换行 "\n" 换成空格 ' '
text = text.replace("\n",' ')

#将'.'换成' '
text = text.replace('.',' ')

#将','换成' '
text = text.replace(',',' ')

#将'--'换成' '
text = text.replace('--',' ')

#将'*'换成' '
text = text.replace('*',' ')

#将'!'换成' '
text = text.replace('!',' ')

#将字符串拆分成列表     
words = text.split(' ')

#创建一个新列表存储满足条件的值
newWords = []

#过滤空字符串''
while '' in words:
    words.remove('')

for k,word in enumerate(words):

    #去掉单词首尾' '
    word = word.strip()
    
    #删除包含'ea'的单词
    if "ea" in word:
        #words.remove(word)
        continue

    #大小写字母反转
    word = word.swapcase()

    newWords.append(word)

#升序排列
newWords = sorted(newWords)

print(newWords)