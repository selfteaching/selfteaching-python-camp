from re import compile

key = r"<h1>hello world<h1>"#源文本
p1 = r"<h1>+<h1>"#我们写的正则表达式，下面会将为什么
pattern1 = compile(p1)
print(pattern1.findall(key))

key = r"afiouwehrfuichuxiuhong@hit.edu.cnaskdjhfiosueh"
p1 = r"chuxiuhong@hit\.edu\.cn"
pattern1 = compile(p1)
print(pattern1.findall(key))

key = r"http://www.nsfbuhwe.com and https://www.auhfisna.com"#胡编乱造的网址，别在意
p1 = r"https*://"#看那个星号！
pattern1 = compile(p1)
print(pattern1.findall(key))

#key = r"<html><body><h1>hello world<h1></body></html>"#这段是你要匹配的文本
#p1 = r"(?<=<h1>).*(?=<h1>)"#这是我们写的正则表达式规则，你现在可以不理解啥意思
#pattern1 = re1.compile(p1)#我们在编译这段正则表达式
#matcher1 = re1.search(pattern1,key)#在源文本中搜索符合正则表达式的部分
#print(matcher1.group(0))#打印出来