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

#1、Replace 'better' with 'worse' in text.
text1 = text.replace('better', 'worse', text.count('better'))

#for test
#print(text1)

#2、Remove the words which include the substring 'ea' in s.
L = text1.split()
i = 0
while(i < len(L)):
    if 'ea' in L[i]:
        del L[i]
    i = i + 1

#for test
#print(L) 
#print(f'The length of L is {len(L)}')

s = " "
text2 = s.join(L)

#for test
#print(text2)

#3、Swapcase the string text2
text3 = text2.swapcase()

#for test
#print(text3) 

#4、cSort the words and print out
s1 = text3.replace('*', '', text3.count('*'))
text4 = s1.replace('-', '', s1.count('-'))

#print(text4) 

L1 = text4.split()
L1.sort()

#for test
#print('The sorted L1 is:\n', L1)

s2 = " "
text5 = s2.join(L1)
print(text5)