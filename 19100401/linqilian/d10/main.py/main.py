
输出 tang300.json 文件中词频前 20 的词和词频数 
   import os 
   os.chdir(r'D:\用户目录\我的文档\GitHub\selfteaching-python-camp\19100401\Newonefromhere\d10') 
   f = open('tang300.json','r',encoding='utf8') 
   text2 = f.read() 
   resl_cn = stats_text_cn(text2,20) 
   f.close() 
   print(resl_cn)  No newline at end of file  

