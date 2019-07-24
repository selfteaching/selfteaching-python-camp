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
#1将字符串样本text里的better全部转换为worse
text2=text.replace('better','worse')
print('------------------------------------[1]-------------------------------------')
#2从第2步结果里剔除包含ea的单词
text3=text2.split()                         #用空格分割第二步得到的文本字符串
text4=[]                                    #新建一个列表存放剔除含ea的单词
for word in text3:                          #遍历第二步得到的单词列表，不含ea的单词则加入新的列表中
       if 'ea' not in word:
               text4.append(word)
text5=' '.join(text4)
print('------------------------------------[2]-------------------------------------')
#3把第三步结果的大小字母翻转
text6=text5.swapcase()
print('------------------------------------[3]-------------------------------------')
#4把第四步结果所有的单词从a-z升序排列并输出
text7=text6.replace(',',' ').replace('--',' ').replace('*',' ').replace('!',' ').replace('.',' ')
text8=text7.split()
sorted(text8,key=str.lower)
print(text8)
print('------------------------------------[4]-------------------------------------')        
         



