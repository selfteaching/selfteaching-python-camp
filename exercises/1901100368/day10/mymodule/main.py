import stats_word

with open('tang300.json',encoding='UTF-8') as a:
    file_string = a.read()
a.closed

try:
    string_resulta = stats_word.stats_text_cn(file_string,20)
    print(string_resulta)
except ValueError:
    print("please input string type!")