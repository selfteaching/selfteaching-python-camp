from mymodule import stats_word
import os

with open(os.getcwd() + "/d09/tang300.json" ,'r') as f:
    text = f.read()

if __name__ == "__main__":
    try:
        print(stats_word.stats_text(text,100))
    except TypeError:
        print("Oops!  That was no string.  Try again...")
    except AttributeError:
        print('list object has no attribute lower')

