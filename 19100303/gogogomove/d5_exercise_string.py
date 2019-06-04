s = '''The Zen of Python, by Tim Peters
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
Namespaces are one honking great idea -- let's do more of those!'''
s.find('better')
s.replace('better','worse')
supdate = s.replace('better','worse')
# supdate is the answer for the 1st task

# try to make the text more clean
supdateagain = supdate.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ').replace('!',' ')
# convert it into a list to handle next 
su = supdateagain.split()
k1="ea"
k2=[]
for i in su:
    if i.find(k1)<0: # to track those words without ‘ea’
        k2.append(i) # then put the targets(wihtout"ea" words into the new list k2)
print(k2)
# to complete the next task, first have to convert the above k2-which is a list into string
k3 = ' '.join(k2) # strange expression/function for me, but okay now first to finish it!
print(k3)
# then to sawp the case as you asked
k4=k3.swapcase()
print(k4)
#before sort it , first convert it back into list
k5 = list(k4)
print(k5)

# notice something is wrong, the single letters shows after the text. strange, but i decide to move on first, let my coach to find out why.
k5.sort()
print(k5)
