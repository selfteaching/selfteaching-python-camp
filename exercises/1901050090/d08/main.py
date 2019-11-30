from  mymodule import stats_word
import traceback
if  __name__ == "__main__":
  try:
      result_text=stats_word.stats_text(1)
  except Exception as e:
     print('test_traceback-->',e)
     print(traceback.format_exc())
 
  