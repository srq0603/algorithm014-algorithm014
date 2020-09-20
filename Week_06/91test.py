#!/usr/bin/env python      
# -*- coding: utf-8 -*-
#91.解码问题
class Solution(object):
    def numDecodings(self, s):

        if not s or s[0]=='0':
            return 0
        if len(s) == 1:
            return 1

        dp = [0]*(len(s)+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1,len(s)):
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    dp[i+1] = dp[i-1]
                else:
                    return 0
            else:
                if 10 < int(s[i-1:i+1]) < 27:
                    dp[i+1] = dp[i-1]+dp[i]
                else:
                    dp[i+1] = dp[i]
        return dp[-1]

if __name__ == '__main__':
    a = Solution().numDecodings("110")
    print(a)