
print("hello world")


for n in range(2, 100): #range(2,100)表示含左侧2，不含右侧100，是不是第三次看到这个说法了？
    if n == 2:
        print(n)
        break
    for i in range(2, n):
        if (n % i) == 0:
            break
    else:                  # 这里目前你可能看不懂…… 但，先关注结果吧。
        print(n)    

print("hello world")


html = """
<html lang="en">
    <head>
        <title>PyQuery学习</title>
    </head>
    <body>
        <ul id="container">
            <li class="object-1"/>
            <li class="object-2"/>
            <li class="object-3"/>
        </ul>
    </body>
</html>

"""

from pyquery import PyQuery
doc = PyQuery(html)
print(doc)

