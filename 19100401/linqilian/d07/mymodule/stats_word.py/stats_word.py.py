import re  
 2 +  from collections import Counter 
 3 +  import numpy 
 4 +  
 
  def stats_text_en(it): #counts and ranks english words, return array 
  			 #has to do numpy array otherwise don't know 
 
 
 	wq={} 
   
 
 	for i in it.split(): 
   		j = re.sub(r'[^a-zA-Z\']',"",i) 
   		if j not in wq: 
  			wq[j] = 1 
   		else: 
   			wq[j] +=1 
   
 
   	k = Counter(wq) 
   	#print(k) 
   	t=[(v,k) for k,v in k.items()] 
   	a = [ k for v, k in sorted(t,reverse=True)] 
  	a = numpy.array(a) 
  	return a 
  
 
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
   
 
   a = stats_text_en(text) 
   print("\n\n\nreturend type: %s \n\ncontent %s"%(type(a),a)) 
    

#该函数用于统计字符串中每个汉字出现的个数。需要输入字符串，输出的结果是按照降序排列的以中文汉字及其字频为元组的一个字典 
   def stats_text_cn(str): 
       #移除字符串头尾的空格和换行符号 
       str=str.strip() 
       #去除所有的标点符号 
       biaodian='。，“”…，——，？：、！《》' 
       for i in biaodian: 
           str=str.replace(i,'') 
       #目前字符串str中应该只包含汉字，下面对汉字字符串进行统计和 
       #方法与统计单词是后基本一样，因为这里是统计中文汉字个数，所以每个汉字都是一个元素， 
       #于是没有必要去将字符串在转换成一个单词列表 
       char_dict={} 
       for char in str: 
           if char in char_dict: 
               count=char_dict[char] 
           else: 
               count=0 
           count +=1 
           char_dict[char]=count 
       char_dict=sorted(char_dict.items(),key=lambda x:x[1],reverse=True) 
       #输出最后的结果 
       print(char dict)

       def stats_text(text):
           mdict={}
           mdict=stats_text(text)
           print(mdict)

       if __name__=='__main__':
           main()
                      
                      