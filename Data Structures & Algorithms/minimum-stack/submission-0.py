class MinStack:

    def __init__(self):
        self.stack = [] # store all pushed values
        self.minStack = [] # store min so far at each level
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(val,self.minStack[-1])
        self.minStack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
