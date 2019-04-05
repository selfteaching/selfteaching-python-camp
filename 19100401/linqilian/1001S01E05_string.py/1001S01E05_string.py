
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
In the face of ambxiguity,refuse the temptation to guess.
There should be one --and preferably only one --obvious way to do it.
Althoug that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let't do more of those!
'''

print('****************************************\n第一步：better替换成worse:\n****************************************') 
 text=text.replace('better','worse') 
 print(text) 
 
 
 
 
 print('****************************************\n第二步：将字符串样本text里英文单词中包含ea的英文单词剔除:\n****************************************') 
 new_list_1 = text.split() 
 str1="ea" 
 str2=[] 
 for i in new_list_1: 
     if i.find(str1) < 0: 
         str2.append(i) 
 print(str2) 
 
 
 print('****************************************\n第三步：大小写字母转换:\n****************************************') 
 text=text.swapcase() 
 print(text) 
 
 
 print('****************************************\n第四步：将所有单词按a，...z升序排列:\n****************************************') 
 new_list_2=text.split() 
 new_list_2.sort() 
 print(new_list_2) 

          
