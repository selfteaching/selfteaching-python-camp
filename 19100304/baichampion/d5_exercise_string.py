text = '''
The Zen of Python, by Tim Peters.
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
print(text.replace("better","worse")) #在做文本替换时，一定要记得把替换的词
                                      #用单引号或者双引号括起来，要替换的词
                                      # 就是一个未定义的变量。（新手如我，一
                                      # 徘徊于这个错误的操作）

text_0 = text.replace("better","worse")
print(text_0.replace("ea",""))         #起初，一直想着是用strip还是remove还
                                        #是用pop抑或用clear，但是看过它们的
                                        # 特性之后，作为新手的我，还是不知道
                                        # 怎样下手为好，最后面google的时候
                                        # 无意看到了一个类似的问题，所以我也
                                        # 干脆用替换的理念把ea删除，把它替换
                                        # 成“none”。嗯，很巧妙                   

text_1 = text_0.replace("ea","")
print(text_1.swapcase())                #这一步挺简单，对于新手来说，学会怎样调用函数
                                        #是一种能力，同时通过用知道有这样一个字母大小
                                        # 交换的内置函数（build-in function），同时
                                        #也是在不断熟悉变量的使用
text_2 = text_1.swapcase()
text_3 = text_2.split(' ')              #如果这里不用split（' '）把单词分离开来，最后面
                                        #整个输出就全部是单个母的排序
print(sorted(text_3))                   #字符串容器是不可变的（immutable），所以只能是
                                        #将整个文本视为单独的一个个体，代入函数进行
                                        #运算