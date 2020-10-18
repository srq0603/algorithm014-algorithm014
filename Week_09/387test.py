#!/usr/bin/env python      
# -*- coding: utf-8 -*-
#387.字符串中的第一个唯一字符
import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)

        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1