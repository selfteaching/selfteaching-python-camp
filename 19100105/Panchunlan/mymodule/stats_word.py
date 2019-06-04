
def stats_text():  

    from d6_exercise_stats_word import stats_text_en,stats_text_cn
    return dict(stats_text_en(),**stats_text_cn())           
  
def main():
    mdict={}
    mdict=stats_text()
    print(mdict)  

if __name__=='__main__':
    main()
    print



