
import re 
from collections import Counter
import numpy

def stats_text_en(it, n): #counts and ranks english words, return array
			 #has to do numpy array otherwise don't know
	try:
		wq={}

		for i in it.split():
			j = re.sub(r'[^a-zA-Z\']',"",i)
			if j not in wq:
				wq[j] = 1
			else:
				wq[j] +=1

		k = Counter(wq).most_common(n)
		#print(k)
		#t=[(v,k) for k,v in k.items()]
		#a = [ k for v, k in sorted(t,reverse=True)]
		#a = numpy.array(a)
		return k
	except TypeError:
		print("From module:\tThe type of input is not a string")
	except ValueError:
		print("From module:\tThe value of input is not correct")
	except AttributeError:
		print("From module:\tThe type of input does not have this type of attribute")

#text = '''
#The Zen of Python, by Tim Peters
#Beautiful is better than ugly.
#Explicit is better than implicit.
#Simple is better than complex.
#Complex is better than complicated.
#Flat is better than nested.
#Sparse is better than dense.
#Readability counts.
#Special cases aren't special enough to break the rules.
#Although practicality beats purity.
#Errors should never pass silently.
#Unless explicitly silenced.
#In the face of ambxiguity, refuse the temptation to guess.
#There should be one-- and preferably only one --obvious way to do it.
#Although that way may not be obvious at first unless you're Dutch.
#Now is better than never.
#Although never is often better than *right* now.
#If the implementation is hard to explain, it's a bad idea.
#If the implementation is easy to explain, it may be a good idea.
#Namespaces are one honking great idea -- let's do more of those!
#一二三四五六七八、七六五四三二一！八个姑娘走来走去，我的姑娘在哪里？哎～哎～在哪里～诶！我的姑娘在哪里？ 姐姐好啊、妹妹好啊～哪个漂亮哪个好！北京好啊、新疆好啊～哪里有你哪里好！
#'''

#a = stats_text_en(text)
#print("\n\n\nreturend type: %s \n\ncontent %s"%(type(a),a))
#
## PART 2 below #
#
#tcn='一二三四五六七八、七六五四三二一！八个姑娘走来走去，我的姑娘在哪里？哎～哎～在哪里～诶！我的姑娘在哪里？ 姐姐好啊、妹妹好啊～哪个漂亮哪个好！北京好啊、新疆好啊～哪里有你哪里好！'
def stats_text_cn(it, count):   #counts and ranks chinese chars, return array
			 #has to do numpy array otherwise don't know
	its = re.sub(r'[。！、？～， !*-.\n\',a-zA-Z]',"",it)
	k = Counter(its).most_common(count)
	#print(k)
	#t=[(v,k) for k,v in k.items()]
	#print("items:\n",t)
	#print("sorted:\n",sorted(t,reverse=True))
	#a = [ k for v, k in sorted(t,reverse=True)]
	#print("sorted a:\n",a)
	#a = numpy.array(a)
	return k
#print("\n\n\nInput text in Chinese:\n",tcn)
#ac = stats_text_cn(tcn)
#print("\n\n\nreturend type: %s \n\ncontent %s"%(type(ac),ac))
#print('原始例子是“我妹妹现在在北京”。字数重复的次数过少')

def stats_text(it, n): # counts Chinese characters and English words
                    # returns combined 
	se = stats_text_en(it, n)
	#print(se)
	sc = stats_text_cn(it, n)
	#print(sc)
	return se+sc

if __name__ == "__main__":
	stats_text(text, 100)

