
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



import  re
a=re.sub(r'[^A-Za-z]',' ',text)
print(a)
print()



str=a.split(' ')
print(str)
print()


str_list=list(str)



for i in str_list:
    if i=='':
        str_list.remove(i)
print(str_list)
print()

char_dict={}



for char1 in str_list:
      if char1 in char_dict:
          count=char_dict[char1]
      else:
         count=0
      count=count+1
      char_dict[char1]=count
 

print(sorted(char_dict.items(),key=lambda k:k[1],reverse=True))

