def stats_text_en(text):  
    '''统计参数text中每个英⽂文单词出现的次数，最后返回⼀个按词频降序排列列的数组'''
    import re
    a = re.sub('[^a-zA-Z \n]','',text)
    b = a.split()
#print('正常的英文单词 ==>',b)
    counter = {}
#word_set = set(b)
    for word in b:
        counter[word] = b.count(word)
    c=sorted(counter.items(),key=lambda item:item[1], reverse=True) 
    for x in c:
        print(x)
    
def stats_text_cn(text):
    '''定义一个统计参数中每个中文单词出现的次数，最后返回一个按词频降序排列的数组'''
    cn_elements = []
    for cn_element in text:
        if '\u4e00' <= cn_element <= '\u9fef':
            cn_elements.append(cn_element) 
    counter = {}
    cn_element_set = set(cn_elements)
    for element in cn_element_set:
        counter[element] = cn_elements.count(element)
    return sorted(counter.items(),key = lambda x:x[1],reverse = True)