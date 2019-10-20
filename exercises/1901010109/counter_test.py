import re

words = re.findall( r'\w+', open('hamlet.txt').read().lower() )