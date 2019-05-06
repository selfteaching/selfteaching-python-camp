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