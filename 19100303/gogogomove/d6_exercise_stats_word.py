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
Namespaces are one honking great idea -- let's do more of those! '''
text_cn = '''抬头望 朵朵云是鹤家乡；
鹤在哪 望眼欲穿不见云；
云在哪 黄鹤一去不复返，白云千载空悠悠。'''
def status_text_en(): # create the function to recive text as the argument
cleantext = text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ').replace('!',' ')
# convert it into a list to handle next 

texttext=cleantext.split()  # covert into list 
counts = {} #  create a dictionary
for word in texttext:   
    counts[word] = counts.get(word, 0) + 1
countsList = list(counts.items())
countsList.sort(key=lambda x:x[1], reverse=True) # counting and sort

for i in range(200):
    word, count = countsList[i]
    print('{}{}'.format(word,count))

## for chinest text 
def status_text_cn(): # create the function to recive text as the argument
cleantext_cn = text_cn.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ').replace('!',' ')
# convert it into a list to handle next 

texttextcn=cleantext.split()  # covert into list 
counts = {} #  create a dictionary
for word in texttextcn:   
    counts[word] = counts.get(word, 0) + 1
countsList = list(counts.items())
countsList.sort(key=lambda x:x[1], reverse=True) # counting and sort

for i in range(200):
    word, count = countsList[i]
    print('{}{}'.format(word,count))