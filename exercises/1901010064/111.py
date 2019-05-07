def stats_text_cn(text):
    """统计参数中每个中文汉字出现的次数，最后返回一个按字频降序排列的数组"""
    word_list=[]
    word_dict={}
    exclude_str=",。？！（）《》，、#*<>"
    for line in fileIn:
        for char in line:
            word_list.append(char)
    
    for char in word_list:
        if char not in exclude_str:
            if char.strip() not in word dict:
                word_dict[char]=1
            else:
                word_dict[char]+=1
        # 排序
     #   x[1]是按字频排序，x[0]则是按字排序
    lstWords = sorted(word_dict.items(), key=lambda x:x[1],  reverse=True) 
   
     # 输出结果 (前100)
     print ('字符\t字频')
     print ('=============')
     for e in lstWords[:100]:
         print ('%s\t%d' % e)
text_0=stats_text_cn("我和你你和他他和她她和她")
print(text_0)