#!/usr/bin/env python      
# -*- coding: utf-8 -*-
#柠檬水找零
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five =  ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if five and ten:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five = five -3
                else:
                    return False
        return True