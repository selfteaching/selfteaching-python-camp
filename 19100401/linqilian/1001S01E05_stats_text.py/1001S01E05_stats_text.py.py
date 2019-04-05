text = ''' 
2 The Zen of Python, by Tim Peters 
3 Beautiful is better than ugly. 
4 Explicit is better than implicit. 
5 Simple is better than complex. 
6 Complex is better than complicated. 
7 Flat is better than nested. 
8 Sparse is better than dense. 
9 Readability counts. 
10 Special cases aren't special enough to break the rules. 
11 Although practicality beats purity. 
12 Errors should never pass silently. 
13 Unless explicitly silenced. 
14 In the face of ambxiguity, refuse the temptation to guess. 
15 There should be one-- and preferably only one --obvious way to do it. 
16 Although that way may not be obvious at first unless you're Dutch. 
17 Now is better than never. 
18 Although never is often better than *right* now. 
19 If the implementation is hard to explain, it's a bad idea. 
20 If the implementation is easy to explain, it may be a good idea. 
21 Namespaces are one honking great idea -- let's do more of those! 
22 ''' 
23 text=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')#将非英文字符替换为空格 
24 text=text.lower()#将所有英文字符改为小写 
25 text=text.split()#以空格拆分为独立的单词 
26 zidian={} 
27 for i in text:  #将字符串转换为字典 
28     count=text.count(i) 
29     r1={i:count} 
30     zidian.update(r1) 
31     #print(i,'',count ) 
32 print(zidian) 
33 print('*****************************\n排序\n*****************************') 
34 zidian1=sorted(zidian.items(),key=lambda x:x[1],reverse=True) #按照单词出现次数，从大到小排序 
35 print(zidian1) 
