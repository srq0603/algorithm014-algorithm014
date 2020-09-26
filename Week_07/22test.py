#!/usr/bin/env python      
# -*- coding: utf-8 -*-
#22.括号生成
class Solution:
    def generateParenthesis1(self, n): #解法一：动态规划
        if n == 0:
            return []
        total_l = []
        total_l.append([None])    # 0组括号时记为None
        total_l.append(["()"])    # 1组括号只有一种情况
        for i in range(2,n+1):    # 开始计算i组括号时的括号组合
            l = []
            for j in range(i):    # 开始遍历 p q ，其中p+q=i-1 , j 作为索引
                now_list1 = total_l[j]    # p = j 时的括号组合情况
                now_list2 = total_l[i-1-j]    # q = (i-1) - j 时的括号组合情况
                for k1 in now_list1:
                    for k2 in now_list2:
                        if k1 == None:
                            k1 = ""
                        if k2 == None:
                            k2 = ""
                        el = "(" + k1 + ")" + k2
                        l.append(el)    # 把所有可能的情况添加到 l 中
            total_l.append(l)    # l这个list就是i组括号的所有情况，添加到total_l中，继续求解i=i+1的情况
        return total_l[n]

    def generateParenthesis2(self, n): #解法二：回溯法
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        cur_str = ''

        def backtrack(cur_str, left, right, n):
            if len(cur_str) == 2 * n:
                res.append(cur_str)
                return

            if left < n:
                backtrack(cur_str + "(", left + 1, right, n)
            if right < left:
                backtrack(cur_str + ")", left, right + 1, n)

        backtrack(cur_str, 0, 0, n)
        return res

if __name__ == '__main__':
    a = Solution().generateParenthesis(3)
    print(a)
