from mymodule import stats_word

    
try:
    result = stats_word.stats_text("dfj", 899)
    print(result) 
except ValueError as ve:
    print(type(ve))
    print(ve)
    # print(ve.args)