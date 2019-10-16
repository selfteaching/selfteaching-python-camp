#统计参数中每个英文单词出现的次数，最后返回一个按词频降序排列的数组
def stats_text_en(text):
    liebiao=text.split()
    a=[]
    symbols='.-*!,'
    for b in liebiao:
        for symbol in symbols:
            b=b.replace(symbol,'')
        if len(b):
           a.append(b)

    counter={}
    seta=set(a)
    for a1 in seta:
        counter[a1]=a.count(a1)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)


#统计参数中每个中文汉字出现的次数
def stats_text_cn(text):
    text_character=[]
    for character in text:
        if '\u4e00'<=character<='\u9fff':
            text_character.append(character)
    
    counter={}
    set_cn=set(text_character)
    for set_cn1 in set_cn:
        counter[set_cn1]=text_character.count(set_cn1)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)
    

en_text='''
asada afaff wffa, agrwe.
gssdhc -- *yfhsdhci*, frdcsc!
'''

cn_text='''
自学训练营
'''

if __name__ == '__main__':
   en_result=stats_text_en(en_text)
   cn_result=stats_text_cn(cn_text)
   print("统计单词出现次数——\n",en_result)
   print("统计中文出现次数——\n",cn_result)