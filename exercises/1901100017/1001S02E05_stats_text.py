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

replace1 = text.replace("\n","")
replace2 = replace1.replace("."," ")
replace3 = replace2.replace(",","")
replace4 = replace3.replace("--","")
replace5 = replace4.replace("*","")
replace6 = replace5.replace("  "," ")
replace7 = replace6.replace("!","")
replace8 = replace7.replace("'s"," is")
replace9 = replace8.replace("doit","do it")
replace10 = replace9.replace("aren't","are not")

str1 = replace10.split(" ")
str2 = [item.lower() for item in str1]
dic = {}
for i in str2:
    if i in dic:
        dic[i] = dic[i] +1
    else:
        dic[i] = 1
print(dic)

sort1 = sorted(dic.items(),key = lambda x:x[1],reverse = True)
print(sort1)
