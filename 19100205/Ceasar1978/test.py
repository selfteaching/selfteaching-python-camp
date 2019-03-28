
def stats_text_en(text):
    
    if not isinstance(text,str):
        raise ValueError('输入的不是文本格式，请重新输入：')
    
    text = text.replace('.', '').replace('!', '').replace('--', '').replace('*', '').replace(',', '').replace('(', '').replace(')', '').replace(';', '').replace(':', '').replace('\'', '').replace('?', '').replace('_', '').replace('-', '').replace('/', '') .replace('[', '') .replace(']', '') .replace('\\', '') .replace('\"', '').replace('{', '').replace('}', '').replace('\t', '').replace('\n', '').replace('\r\n', '')    
    
# 以上替换去除各种标点符号
    list_text = text.split() # 将字符串转换为列表

    a = {}
    for i in list_text:
        a[i] = list_text.count(i)
    a = sorted(a.items(),key = lambda x:x[1],reverse = True)
    return a
text = int(input('请输入要统计词频的文本：'))

print(stats_text_en(text))
    
