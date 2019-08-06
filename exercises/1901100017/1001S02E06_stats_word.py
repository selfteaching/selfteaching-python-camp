def stats_text_en(text): # receive an english text and count for different words
    str1 = text.replace(',', '').replace('.', '').replace('--', '').replace('!', '').replace('*', '')
    str2 = str1.split(" ")
    str3 = [item.lower() for item in str2]
    dic = {}
    for i in str3:
        if i in dic:
            dic[i] = dic[i] +1
        else:
            dic[i] = 1
    sort1 = sorted(dic.items(),key = lambda x:x[1],reverse = True)
    print(sort1)

def stats_text_cn(text): # receive a chinese text and count for different word
    cn_text = []
    for word in text:
        if '\u4e00' <= word <= '\u9fff':
            cn_text.append(word)
    dic2 = {}
    str4 = set(cn_text)
    for word in str4:
        dic2[word] = cn_text.count(word)
    sort2 = sorted(dic2.items(), key=lambda x:x[1],reverse = True)
    print (sort2)

choice = input("请输入选择： 1. 英文文本统计； 2. 中文文本统计    ")
if choice == "1":
    text = input("请输入英文文本：")
    stats_text_en(text)
elif choice =="2":
    text = input("请输入中文文本：")
    stats_text_cn(text)
else:
    print("error, end")