dic = {'a':1,'b':2,'c':3}

import matplotlib.pyplot
import numpy

# Fixing random state for reproducibility
numpy.random.seed(19680801)


matplotlib.pyplot.rcdefaults()
fig, ax = matplotlib.pyplot.subplots()

# Example data
word = []
frequency = []
for i in dic:
    word.append(i)
    frequency.append(dic[i])

y_pos = numpy.arange(len(word))

error = numpy.random.rand(len(word))

ax.barh(y_pos, frequency, xerr=error, align='center',
        color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(word)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('词语出现次数')
ax.set_title('你刚才所发文章的词频统计')
matplotlib.pyplot.show()