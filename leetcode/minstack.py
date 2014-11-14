'''
Created on 2014-11-13

@author: Administrator
'''

class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
        
    # @param x, an integer
    # @return an integer
    def push(self, x):
        n=len(self.stack)
        if n == 0:
            self.minstack.append(x)
        else:
            last = self.minstack[-1]
            if x <= last:
                self.minstack.append(x)
        self.stack.append(x)

    # @return nothing
    def pop(self):
        if len(self.stack) > 0 and self.stack.pop() == self.minstack[-1]:
            self.minstack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):     
        return self.minstack[-1]
        

if __name__ == '__main__':
    minstack = MinStack()
    minstack.push(7)
    minstack.push(6)
    minstack.push(4)
    minstack.push(9)
    minstack.push(2)
    minstack.push(1)
    minstack.push(12)
    print minstack.getMin()
    print minstack.top()
    minstack.pop()
    minstack.pop()
    print minstack.getMin()
    minstack.pop()
    minstack.pop()
    print minstack.getMin()
    
