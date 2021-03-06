#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-

import re

pat_suma = re.compile(r'(\d+)\+(\d+)')


def sum_eval(s):
    if pat_suma.search(s):
        match = pat_suma.search(s)
        left_op = int(match.group(1))
        right_op = int(match.group(2))
        return left_op + right_op
    return None


def sum_eval2(s):
    match = pat_suma.search(s)
    if match:
        left_op = int(match.group(1))
        right_op = int(match.group(2))
        return left_op + right_op
    return None


def sum_eval3(s):
    if match := pat_suma.search(s):
        left_op = int(match.group(1))
        right_op = int(match.group(2))
        return left_op + right_op
    return None


sample = 'La suma de 10+15'
assert sum_eval3(sample) == 25
print(sum_eval3(sample))
