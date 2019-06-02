from stats_word import stats_text_cn
#stats_text_cn(1234)

while True:
    try:
        x = input("Please enter a text: ")
        stats_text_cn(x)
        break
    except ValueError:
        print("Oops! Argument text must be <class 'str'>  Try again...")