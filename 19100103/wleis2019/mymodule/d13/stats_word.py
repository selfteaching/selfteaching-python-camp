

import stats_word

import typing
import sys
import json
import os
import re,argparse,collections

def stats_text_cn(text):

    return collections.Counter(text).most_common(100)
