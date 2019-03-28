import mymodule.stats_word
text = input("请输入要统计词频的文本：")
try:
    if not isinstance(text,str):
        raise ValueError()
    
except ValueError:
    print('输入的不是文本格式，请重新输入：')
print(mymodule.stats_word.stats_text(text))