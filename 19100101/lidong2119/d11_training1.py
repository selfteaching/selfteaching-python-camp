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
yag = yagmail.SMTP(sender,password,smtp)
yag.send(recipient,'lidong2119 d11',statString)
>>>>>>> cf86c537e790ffb7f78df7821ac287627dc4bbc6
