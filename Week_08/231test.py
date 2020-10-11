#!/usr/bin/env python      
# -*- coding: utf-8 -*-
#231.2的幂
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        return n & (-n) == n