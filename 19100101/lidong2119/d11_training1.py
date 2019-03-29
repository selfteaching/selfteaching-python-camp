import requests
# import yagmail
from pyquery import PyQuery 
from mymodule import stats_word

def stats(url):
    response = requests.get(url)
    document = PyQuery(response.text)
    content = document('#js_content').text()

    statList = stats_word.stats_text(content,100)
    statString = ''.join(str(i) for i in statList)
<<<<<<< HEAD
    return statString
=======

    return statString
>>>>>>> c56b148f08ae89b232f40c5c96bdadbcdf083d2d
