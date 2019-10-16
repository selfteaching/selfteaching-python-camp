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
#print (text)
print(text.replace("better","worse"))
text = text.replace("better","worse")                   #replace the "better" with "worse"
text = text.replace("--","")
text = text.replace(".","")
text = text.replace("!","")
text = text.replace(",","")
text = text.replace("*","")
text1 = text.split()
templist = []
#print(text1)
for i in text1:
    #print(i.find("ea"))
    if i.find("ea") >= 0:       #find the words which contain "ea"
        #print(i)
        templist.append(i)
#print(templist)   
step3 = [x for x in text1 if x not in templist]                   #del the words which contain "ea"
#print (step3)

step4 = []                                                        #my son told me this good method,so I change my way to this.
for i in step3:
        i=i.swapcase()
        step4.append(i)
'''
step4 = []                                                        #use two fors cycles to reverse the letters of the list of step3
for i in step3:
        temp = ""
        for j in i:
                if j.islower():
                        j = j.upper()                             
                elif j.isupper():
                        j = j.lower()
        #print(j)
                temp = temp + j
        step4.append(temp)
'''
step4.sort(reverse=True)
print(step4)