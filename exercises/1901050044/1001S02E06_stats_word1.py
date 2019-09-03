def stats_text_cn(text):
    punctuation = ['，','。','……','——','？','！','；','“','”',':','《','》','\n']
    for i in punctuation:
        text = text.replace(i," ")
    text1 = '' 
    for char in text: 
        text1 = text1 + char + ' ' #给每个汉字中间加上空格
    list1 = text1.split(' ') #将string转换为列表，以空格分割
    for char in list1:
        if '' in list1:
            list1.remove('') #去除列表中空字符
    char_count = {}
    for char in list1:
        if not char in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    char_count = sorted(char_count.items(), key = lambda item :item[1],reverse=True)
    return char_count
text = '''
说着付出生命的誓言， 回头看看繁华的世界， 爱你的每个瞬间， 像飞驰而过的地铁； 说过不会掉下的泪水， 现在沸腾着我的双眼， 爱你的虎口我脱离了危险。
'''
print(stats_text_cn(text))