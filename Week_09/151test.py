#!/usr/bin/env python      
# -*- coding: utf-8 -*-
#151.翻转字符串里的单词
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(reversed(s.split()))