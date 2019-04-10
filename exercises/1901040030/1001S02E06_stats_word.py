text = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

text2 = '''
有记者提问，不久之前，第九轮中美经贸高级别磋商顺利结束，但美国方面有声音提出，对中国所作出的贸易承诺并不满足。
对此，陆慷表示，关于刚刚结束的中美经贸磋商情况，双方都已经发布了有关消息。
就他所掌握的情况，现在中美双方这一轮磋商确实取得了新的实质性进展，双方也都表现出了愿意按照中美元首2018年12月1日在阿根廷会晤中达成的共识，尽快完成磋商的积极意愿。
陆慷说，就中方而言，我们还是希望双方能够按照两国元首的共识，在相互尊重、平等互利的基础上，妥善地解决双方的关切，达成一个双方都能满意的结果。
“在这过程中，可能不同的方面不时会有这样那样的声音出来，具体的情况建议你向主管部门了解。”
'''

def stats_text_en (text:'输入的文本') -> list:
    #先转换成列表
    text_list=text.replace('.','').replace('--','').replace('*','').replace('!','').split()
    #定义一个字典，遍历列表，如果列表的元素在字典的key里面，key的value+1，不在key里，key的value=1
    text_dict={}
    for word in text_list:
        if word in text_dict.keys():
            text_dict[word]=text_dict[word]+1
        else:
            text_dict[word]=1
    #将字典的items已元祖的形式转换成列表，进行排序
    text_list2=sorted(text_dict.items(),key=lambda item:item[1],reverse=True)
    print(text_list2) 

def stats_text_cn (text:'输入的文本') -> list:
    #先转换成列表
    text_list=text.replace('，','').replace('。','').replace('--','').replace('*','').replace('!','').replace('“','').replace('”','').replace('\n','')
    #定义一个字典，遍历列表，如果列表的元素在字典的key里面，key的value+1，不在key里，key的value=1
    text_dict={}
    for word in text_list:
        if word in text_dict.keys():
            text_dict[word]=text_dict[word]+1
        else:
            text_dict[word]=1
    #将字典的items已元祖的形式转换成列表，进行排序
    text_list2=sorted(text_dict.items(),key=lambda item:item[1],reverse=True)
    print(text_list2) 

print('输出英文词频')
stats_text_en(text)
print('输出中文词频')
stats_text_cn(text2)
