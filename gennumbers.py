#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gennumbers.py: output numbers in the Format: 0000 with an optional prefix
:)
"""

from itertools import product as count


digits = 4
values = range(10)
prefix = ""
mycount = 10001


## with itertools
def generate_numbers(digits, values, prefix=prefix):
    pins = list(count(values, repeat=digits))
    for i in pins:
        conv2str = (str(w) for w in i)
        conv2str = ''.join(conv2str)
        combined = f'{prefix}{conv2str}'
        print(combined)


## without itertools
def gen_num(mycount, prefix=prefix):
    i = 0
    while (i < mycount):
        out = "{:04d}".format(i)
        combined = f'{prefix}{out}'
        print(combined)
        i +=1

        
gen_num(mycount)
#generate_numbers(digits, values)


