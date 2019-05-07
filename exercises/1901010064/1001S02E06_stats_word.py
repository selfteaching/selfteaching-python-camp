def stats_text_en(text):
    """统计参数中每个英文单词出现的次数，最后返回一个按词频降序排列的数组"""
    a=text.split()
    set1=set(a)
    b=list(set1)
    dir1={}
    for x in range(len(b)):
        dir1[b[x]]=0
        for y in range(len(a)):
            if b[x] ==a[y]:
                dir1[b[x]]+=1
    dir2=sorted(dir1.items(), key=lambda d:d[1], reverse = True)  
    return dir2

text_0=stats_text_en("Beautiful is better than ugly Explicit is better than implicit Simple is better than complex Complex is better than complicated.Flat is better than nested")
print(text_0)

def stats_text_cn(text):
    """统计参数中每个中文汉字出现的次数，最后返回一个按字频降序排列的数组"""
    word_list=[]
    word_dict={}
    exclude_str=",。？！（）《》，、#*<>"
  # 添加每一个字到列表中
    for line in text:
        for char in line:
            word_list.append(char)
    # 用字典统计每个字出现的个数   
    for char in word_list:
        if char not in exclude_str:
            if char.strip() not in word_dict:
                word_dict[char]=1
            else:
                word_dict[char]+=1
     # 排序
     #   x[1]是按降序排序，x[0]则是按升序排序
    lstWords = sorted(word_dict.items(), key=lambda x:x[1],  reverse=True) 
   
     # 输出结果 (前100)
    for e in lstWords[:100]:
         print ('%s\t%d' % e)#这一步不知道什么意思
text_0=stats_text_cn("我和你你和他他和她她和她")
print(text_0)
