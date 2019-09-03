
# coding: utf-8

# In[33]:


text = ''' The Zen of Python, by Tim Peters
Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambxiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those! '''

temp2=(text.lower()).replace('.','').replace('-','').replace('!','').replace(',','').replace('*','').replace('\n',' ').strip().replace("aren't",'are not').replace("'re",' are').replace("'s",' is')
dit={}
lst = temp2.split(' ')
max = 0
maxkey = ""
for item in lst:
    if (dit.get(item, 0)):
        dit[item] = dit[item] + 1
    else:
        dit[item] = 1
    if (dit[item] > max):
        max = dit[item]
        maxkey = item
result=sorted(dit.items(),key=lambda x:x[1],reverse=True)
print(result)

