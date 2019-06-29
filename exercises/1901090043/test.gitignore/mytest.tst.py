import sys
sys.path.append('../')

import jieba
import jieba.analyse
from optparse import OptionParser

USAGE = "usage:    python,python extract_tags.py [file name] -k [top k]"


tags = jieba.analyse.extract_tags(USAGE, topK=2,withWeight = True)

print(tags)