from mymodule import stats_word
import os


with open( os.getcwd() + "/d09/tang300.json" ,'r') as f:
#with open("tang300.json" ,'r') as f:
    text = f.read()

if __name__ == "__main__":
    try:
        print(stats_word.stats_text_cn(text,20))
    except TypeError:
        print("Oops!  That was no string.  Try again...")
    except AttributeError:
        print('Sorry, there is a AttributeError')

       