from mymodule import stats_word
import os

with open( os.getcwd() + "/d09/tang300.json" ,'r') as f: #Vscode当前文件位置定位19011000088文件夹
#with open("tang300.json" ,'r') as f:  pycharm中可以通过文件名称打开文件，其当前文件位置定位为d09文件夹
    text = f.read()

if __name__ == "__main__":
    try:
        print(stats_word.stats_text(text,100))
    except TypeError:
        print("Oops!  That was no string.  Try again...")
    except AttributeError:
        print('list object has no attribute lower')

       