import stats_word

inta_string = "123456789" 
intb_string = 123456789

try:
    string_resulta = stats_word.stats_text(inta_string)
    print(string_resulta)
    string_resultb = stats_word.stats_text(intb_string)
    print(string_resultb)
except ValueError:
    print("please input string type!")