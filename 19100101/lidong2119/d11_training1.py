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

    return statString
