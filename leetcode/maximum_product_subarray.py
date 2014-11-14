'''
Created on 2014-11-14

@author: Administrator
'''
import sys
from Tkconstants import END

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        start = 0
        end = 0
        maxProduct = A[0]
        while start < len(A):
            while start < len(A) and A[start] == 0:
                start += 1
                if maxProduct < 0:
                    maxProduct = 0
            
            end = start + 1
            while end < len(A) and A[end] != 0:
                end += 1
            
            numM = 0
            tmp = 1
            forward = []
            for i in range(start, end):
                if A[i] < 0:
                    numM += 1
                tmp *= A[i]
                forward.append(tmp)
            if numM % 2 == 0 :
                if forward[-1] > maxProduct:
                    maxProduct = forward[-1]
            else:
                backward = []
                tmp = 1
                for i in range(end - 1, start - 1, -1):
                    tmp *= A[i]
                    backward.append(tmp)
                
                for i in range(start + 1, end - 1):
                    maxProduct = max([maxProduct, forward[i - start - 1], backward[end - start - 1 - (i - start) - 1]])
                
                if end - start > 1:
                    maxProduct = max([maxProduct, forward[-2], backward[-2]])
                    
            start = end
        
        return maxProduct

if __name__ == '__main__':
    s = Solution()
    # print s.maxProduct([-2, 0, -1])
    print s.maxProduct([1, 0, -1, 2, 3, -5, -2 ])
