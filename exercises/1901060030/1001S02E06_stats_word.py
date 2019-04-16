t = '''
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

print("Task 1: count words in English\n")
# cleaning data and convert string to list
t2 = t.replace('Peters','Peters.')
t2 = t2.replace('\\n',"")
t2 = t2.replace(' -- '," ")
t2 = t2.replace("."," ")
t2 = t2.replace('\'',"")
t2 = t2.replace('\"',"")
t2 = t2.replace('-',"")
t2 = t2.replace('*',"")
t2 = t2.replace('!',"")

def stats_text_en(text):
    from collections import Counter
    text = ascii(text)
    new_list = text.split(' ')
    new_list1 = []
    for i in new_list:
        new_list1.append(i.lower())
    print(Counter(new_list1))
stats_text_en(t2)

print("\nTask 2: count words in Chinese\n")
c = '吃葡萄不吐葡萄皮不吃葡萄倒吐葡萄皮'
def stats_text_cn(text):
    from collections import Counter
    new_list3 = []
    for i in text:
        new_list3.append(ord(i))
    new_list4 = []
    for i in new_list3:
        new_list4.append(chr(i))
    print(Counter(new_list4))

stats_text_cn(c)


