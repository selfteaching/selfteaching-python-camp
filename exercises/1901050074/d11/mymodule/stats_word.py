from collections import Counter #提供了可哈希对象的计数功能 
import jieba

def stats_text_en(text_en,count):    # 统计文本中英文单词出现的次数，并按词频降序排列，返回数组
    if isinstance(text_en, str)==False:
        raise ValueError('输入的参数为{type(text_en)}类型，非字符串，请重新输入。')
    text1=text_en.replace(',','').replace('.','').replace('!','').replace('*','').replace('-','').replace('?','') #去标点
    text2=text1.lower().split()   #拆分并转字符串

    cnt=Counter()        
    for i in text2:    
        if i.isascii():         
            cnt[i]+=1
    
    return Counter(cnt).most_common(count)
   
# text_en='''
# Beautiful is better than ugly. 
# Explicit is better than implicit. 
# Simple is better than complex. 
# Complex is better than complicated. 
# Flat is better than nested. 
# Sparse is better than dense. '''
# print('测试文本：',text_en)
# print('统计如下：\n',stats_text_en(text_en,5))

def stats_text_cn(text_cn,count):    # 统计文本中中文汉字出现的次数，并按词频降序排列，返回数组
    if isinstance(text_cn, str)==False:
        raise ValueError('输入的参数为{type(text_cn)}类型，非字符串，请重新输入。')
    text1=text_cn.replace('，','').replace('。','').replace('!','').replace('*','').replace('-','').replace('?','') #去标点
    
    list1=''
    for i in text1:
        if u'\u4e00' <= i <= u'\u9fa5': #提取中文汉字           
            list1+=i
    seg_list=jieba.cut(list1,cut_all=False)   #利用jieba精确模式，切分
    #print(", ".join(seg_list))

    cnt=Counter()
    cnt = [word for word in seg_list if len(word) >= 2]
    # for word in seg_list:
    #     if len(word)>=2:
    #         cnt[word]+=1
    
    return Counter(cnt).most_common(count)

# text_cn ='''天下只有两种人。比如一串葡萄到手，一种人挑最好的先吃，另一种人把最好的留到最后吃。照例第一种人应该乐观，因为他每吃一颗都是吃剩的葡萄里最好的；第二种人应该悲观，因为他每吃一颗都是吃剩的葡萄里最坏的。不过事实却适得其反，缘故是第二种人还有希望，第一种人只有回忆。'''
# print('测试文本：\n',text_cn)
# print('统计如下：\n',stats_text_cn(text_cn,10))

def stats_text(text,count):   # 分别调用stats_text_en和stats_text_cn,输出合并词频统计结果
    if isinstance(text, str)==False:
        raise ValueError('输入的参数为{type(text)}类型，非字符串，请重新输入。')
    print(stats_text_en(text,count),'\n',stats_text_cn(text,count))