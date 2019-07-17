# Tasks 5.1
# 1-assign the variable "text" value as a str
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
  If the implementation is hard to explain, it's a bad idea.
  If the implementation is easy to explain, it may be a good idea.
  Namespaces are one honking great idea -- let's do more of those!
  '''

# 2-assign a new variable "changeWords" value using replace to change some words in "text"
changeWords = text.replace('better', 'worse')
# print(changeWords) #checking upon my output value

# 3-goal:delete those words including "ea"

# 3.1 FIND THE KEYWORDS
# question1: can this be proceed by string method? or have to be changed into list?
# explored on campmates' homeworks got confused on why split and why the sequences(flow of control)
# 3.1 question2: the assignment tasks including the procedures, are those sequences indicated the hint/
# guidance on flow of control? I deemed the answer yes and take my movements.
# AS CLOSELY STICKED TO MY QUESTION1 AS POSSIBLE:
# I found one thinking process quite enlightened (19100101 echojce) I copied this works and
# tried some of my experiments. APPERICIATED A LOOOO0T @echojce.

# let's assign a variable "text" the value as follows
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

# 1.1 let's replace better by worse
text1 = text.replace('better', 'worse')

# let's convert it to a list
list1 = text1.split()

# using print(list1) to check whether this worked -- checked

# 1.2 let's try to delete the words with "ea"

str1 = 'ea'
list2 = []
for i in list1:
    if i.find(str1) == -1:  # if not find ea in i, put this i into list2
        list2.append(i)
    else:
        continue  # not break because we should keep looking for qualified i to put into list2
# use: print(' '.join(list2)) to check whether # this showed a text? str?

# 1.3 let's try to use string method --swapcase
# what we have now should be a string right?
# let's check it up
str2 = ' '.join(list2)
# print(str2) showed it worked now.

# now swapcase
text2 = str2.swapcase()
# by checking up :print(text2)-- ok worked

# 1.4 let's try to delete those - . * , ! and sort
# we have to convert to a list?[to be thought later]

list3 = text2.split()  # let's try on list using split method
# this one is used to eliminate the first " ".but how?[to be thought later]
i = 0
for i in range(0, len(list3)):
    list3[i] = list3[i].strip('*-,.!')  # list[i] used to index the position.
    if list3[i] == ' ':
        list3[i].remove(' ')
    else:
        i = i + 1  # still not so clarified. oh my poor math mindset more practice more!
list4 = sorted(list3)

print(' '.join(list4))

# I knew I could make it!!! Ok still some other puzzles need to go explore deeper!
