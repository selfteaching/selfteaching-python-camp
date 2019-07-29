


sample_text = '''
The Zen of Python, by Tim Peters                       


Beautiful is better than ugly. 
Explicit is better than implicit.   Explicit is better than implicit.
Simple is better than complex.       Simple is better than complex.
Complex is better than complicated.    Complex is better than complicated.
Flat is better than nested.             Flat is better than nested.
Sparse is better than dense.            Sparse is better than dense.
Readability counts.                      Readability counts.
Special cases aren't special enough to break the rules.     Special cases aren't special enough to break the rules.
Although practicality beats purity.                      Although practicality beats purity.
Errors should never pass silently.             Errors should never pass silently.
Unless explicitly silenced.                    unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.  
There should be one-- and preferably only one --obvious way to do it.   preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.     you're Dutch.
Now is better than never.                                        Now is better than never.
Although never is often better than *right* now.            Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.  If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.     it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!   Namespaces are one honking great idea -- let's do more of those.
'''


#1. 将字符串样本里的 better 全部替换 worse   

text = sample_text.replace("better", "worse")    
print('将字符串样本里的 better 全部替换成 worse ==', text)

#2. 将单词中包含 ea 的单词剔除                                        
      
words = text.split()                                                    
filtered = []                                        
for word in words:                                     
    if word.find('ea') < 0:      
        filtered.append(word)        
print('将单词中包含 ea 的单词剔除 ==', filtered)        

# 3. 进行大小写翻转                               
swapcased = [i.swapcase() for i in filtered]   
print('进行大小写翻转 ==', swapcased)            

# 4. 单词按 a_z 升序排列                        
print('单词按 a_z 升序排列 ==', sorted(swapcased))       
#print('单词 a_z 降序排列 ==', sorted(swapcased, reverse=True))  
