
# coding: utf-8

# In[117]:


text = ''' The Zen of Python, by Tim Peters
Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambxiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those! '''
text2=text.replace("better","worse")
print(text2)

text3=text2.replace("\n"," ")
#print(text2)
n=text3.count("ea")
print('total %d ea' %n)
j=0
wordea=list()
for i in range(len(text3)):
    if i==0 :
        start=text3.find(" ")+1
    else :
        start=end+1;
    end=text3.find(" ",start)
    word=text3.find("ea",start,end)
    
    if word>0 and j<n:
        j=j+1
        wordea.append(text3[start:end])
        print('%dth ea' %j)
        print(wordea)
    else:
        continue

for t in range(len(wordea)):
    w1=wordea[t]
    text3=text3.replace(w1,"")
print(text3)

text4=text3.swapcase()
print(text4)

temp=text3.replace(",","").replace('.','').replace('-','').replace('*','').replace('!','').strip()
temp1=temp.split(" ")
temp1.sort()
del temp1[0:10]
print(temp1)

