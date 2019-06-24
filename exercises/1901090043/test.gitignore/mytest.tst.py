import re
# encoding:utf-8
key = r"lalala<hTml>hello</Html>heiheihei"
p1 = r"<[Hh][Tt][Mm][Ll]>.+?</[Hh][Tt][Mm][Ll]>"
pattern1 = re.compile(p1)
print(pattern1.findall(key))

key = r"hmat cat hat pat"
p1 = r"[^p]at"#这代表除了p以外都匹配
pattern1 = re.compile(p1)
print(pattern1.findall(key))

pattern = r"\w+@\w+.*(\w+)\.com"  # 匹配邮箱
mt = re.match(pattern, "luosongchao@xxx.yyy.xadad.com")
if mt:
    print(mt.group())
    print(mt.groups())
else:
    print("no match")


text = '''1. 在 1001S02E06_stats_word.py 中定义⼀一个名为 stats_text_cn 的函数，函数接受⼀一 个字符串串 text 作为参数
2. 实现该函数的功能:统计参数中每个中⽂文汉字出现的次数，最后返回⼀一个按字频降序排列列的 数组，很好的开始
3. 为 stats_text_cn 添加注释说明he Zen of Python, by Tim Peters Beautiful is better than ugly.
Explicit is better'''

text1 = '''1. 在 1001S02E06_stats_word.py 中定义⼀一个名为 stats_text_cn 的函数，函数接受⼀一 个字符串串 text 作为参数
2. 实现该函数的功能:统计参数中每个中⽂文汉字出现的次数，最后返回⼀一个按字频降序排列列的 数组，很好的开始
3. 为 stats_text_cn 添加注释说明he Zen of Python, by Tim Peters Beautiful is better than ugly.
Explicit is better'''

#字符串文本按照单词排序
#def stats_text_en(text):
pattern = re.compile( "[A-Z]*[a-z]+")
word_list = re.findall(pattern,text)
dic = {}
for item in word_list:
    if item not in dic:
        dic[item] = 1
    else:
        dic[item] += 1

dic = sorted(dic.items(),key = lambda x:x[1],reverse = True)

print(dic)

dir = {}
pattern1 = re.compile("[\u4E00-\u9FA5]")
new_list = re.findall(pattern1,text1)
for item in new_list:
    item = item.strip()
    if item not in dir:
        dir[item] = 1
    else:
        dir[item] += 1        
    #把汉子装入词典
dir = sorted(dir.items(),key = lambda x:x[1] ,reverse = True)
print(dir)
    
