# -*- coding: utf-8 -*-
# coding:utf-8
import re
text = '''
是一套用于构建用户界面的渐进式框架与其它大型框架不同的是被设计为可以自底向上逐层应用的核心库只关注视图层不仅易于上手还便于与第三方库或既有项目整合另一方面当与现代化的工具链以及各种支持类库结合使用时完全能够为复杂的单页应用提供驱动如果你想在深入学习之前对它有更多了解我们制作了一个视频带您了解其核心概念和一个示例工程如果你已经是有经验的前端开发想知道与其它库框架有哪些区别，请查看对比其它框架
'''

result = {}
# pattern = u'\u6211.*?\u3002'
# pat = re.compile(pattern)

# regex_str = ".*?([\u4E00-\u9FA5])"
# match_obj = re.match(regex_str, text)

#print(match_obj)

#统计英文单词在这段话的出现频次 并且返回
def stats_text_cn(text):
    #str_array= text.split('')
    #print(text)
    #temp = pat.findall(text)
    #print(temp)

    for i in set(text):
        
       result[i] = text.count(i)
    return  sorted( result.items(),key= lambda item:item[1],reverse= True )

print(stats_text_cn(text))


 
 

 

# def findPart(regex, text, name):
#     res=re.findall(regex, text)
#     #if res:
#        # print "There are %d %s parts:\n"% (len(res), name)
#     #for r in res:
#        # print "\t",r.encode("utf8")
#     print(res)
# text ="#who#helloworld#a中文x#"
# #usample=unicode(text,'utf8')
# findPart(u"#[\w\u2E80-\u9FFF]+#", text, "unicode chinese")
