
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

hu_replace = text.replace('better', 'worse')

import re
hu_ea_list = re.split(r"(\W+)", hu_replace)  
for i in hu_ea_list:               
    if 'ea' in i:            
        hu_ea_list.remove(i)      
hu_ea = " ".join(hu_ea_list)

hu_cl = hu_ea.swapcase()

hu_cl_list = re.split(r"\W+",hu_cl)   
hu_cl_list.sort()    
while '' in hu_cl_list:   
    hu_cl_list.remove('')
hu_sort = " ".join(hu_cl_list)

print(hu_sort)