学习笔记
1.python中处理字符串的题目可以转换成处理特定的数组，从而按照处理数组的方法解决问题
2.不同路径2的状态转移方程dp[i][j] = dp[i - 1][j] + dp[i][j - 1];表示向右走和向下走
3.151字符串翻转的题目，利用Python自带函数先将字符串利用split函数按空格进行拆分，然后用reversed进行翻转，再用join进行拼接