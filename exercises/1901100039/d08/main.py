#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 11:06:36 2019

@author: mtattoo
"""

from mymodule import stats_word
import traceback
import logging

text = int(input('请输入文本: '))

logger = logging.getLogger(__name__)

def test_traceback():
    try:
        stats_word.stats_text(text)
    except Exception as errors:
        print('test_traceback :', errors)
        print(traceback.format_exc())

def test_logger():
    try:
        stats_word.stats_text(text)
    except Exception as errors:
        print('test_logger :', errors)
        logger.exception(errors)

if __name__ == "__main__":
    stats_word.stats_text(text)
    test_traceback()
    test_logger()

result = stats_word.stats_text(text)
print('中英文字符统计情况如下：', result)
