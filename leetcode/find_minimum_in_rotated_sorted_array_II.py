'''
Created on 2014年11月14日

@author: Administrator
'''


class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if len(num) <= 0:
            raise RuntimeError("num len <= 0")
        length = len(num)
        for i in range(length - 1):
            if num[i + 1] < num[i]:
                return num[i + 1]
        return num[0]
