#!/usr/bin/env python      
# -*- coding: utf-8 -*-
#买卖股票最佳时机
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        income = 0
        for i in range(1,len(prices)):
            if prices[i] > prices [i-1]:
                income = income + prices[i] - prices[i-1]
        return income