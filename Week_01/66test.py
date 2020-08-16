#!/usr/bin/env pytho      
# -*- coding: utf-8 -*-
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    sums = 0
    for i in digits:
        sums = sums * 10 + i  # 10进制乘以10，进行累积和；
    sums_str = str(sums + 1)
    # print(list(sums_str))
    return map(int, list(sums_str))