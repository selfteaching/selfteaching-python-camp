

# 统计各单词出现的次数
def stats_text_en(text):
    text = text.replace('.', '')
    text = text.replace('!', '')
    text = text.replace('--', '')
    text = text.replace('*', '')
    text = text.replace(',', '') 
    text = text.replace('(', '') 
    text = text.replace(')', '') 
    text = text.replace(';', '') 
    text = text.replace(':', '') 
    text = text.replace('\'', '') 
    text = text.replace('?', '') 
    text = text.replace('_', '') 
    text = text.replace('-', '') 
    text = text.replace('/', '') 
    text = text.replace('[', '') 
    text = text.replace(']', '') 
    text = text.replace('\\', '') 
    text = text.replace('\"', '') 
    text = text.replace('{', '') 
    text = text.replace('}', '')  
    text = text.replace('\t', '') 
    text = text.replace('\n', '') 
    text = text.replace('\r\n', '')    
        
        
        
    # 以上替换去除各种标点符号
    list_text = text.split() # 将字符串转换为列表

    import collections
    m=collections.Counter(list_text)
    return(m)
a = input("请输入要统计词频的文本：")
print(stats_text_en(a))