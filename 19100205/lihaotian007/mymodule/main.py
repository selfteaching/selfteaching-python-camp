import stats_word as sw

int_a = 1234567890
list_b = ['the','0','李','哈','哈']
str_c = 'The work of lihaotian007 , 看起来不错哦'
dict_d = {'李':'0','the':'2','哈':'3'}

print('''please choose the topy of Argument :
[0] int \t[1] list \t[2] string \t[3] dict
''')

a = input()
if a == '0' :
    print('Above is the result of stats_text ',sw.stats_text(int_a),'\n')
    print('Above is the result of stats_text_cn ',sw.stats_text_cn(int_a,int_a),'\n')
    print('Above is the result of stats_text_en ',sw.stats_text_en(int_a,int_a),'\n')
elif a == '2' :
    print('Above is the result of stats_text ',sw.stats_text(str_c),'\n')
    print('Above is the result of stats_text_cn ',sw.stats_text_cn(str_c,str_c),'\n')
    print('Above is the result of stats_text_en ',sw.stats_text_en(str_c,str_c),'\n')
elif a == '1' :
    print('Above is the result of stats_text ',sw.stats_text(list_b),'\n')
    print('Above is the result of stats_text_cn ',sw.stats_text_cn(list_b,list_b),'\n')
    print('Above is the result of stats_text_en ',sw.stats_text_en(list_b,list_b),'\n')
elif a == '3' :
    print('Above is the result of stats_text ',sw.stats_text(dict_d),'\n')
    print('Above is the result of stats_text_cn ',sw.stats_text_cn(dict_d,dict_d),'\n')
    print('Above is the result of stats_text_en ',sw.stats_text_en(dict_d,dict_d),'\n')