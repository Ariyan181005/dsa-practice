class MinStack(object):

    def __init__(self):
        self.st=[]
        self.mn=[]

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.st.append(value)
        if not self.mn:
            self.mn.append(value)
        else:
            self.mn.append(min(value,self.mn[-1]))

    def pop(self):
        """
        :rtype: None
        """
        self.st.pop()
        self.mn.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.st[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mn[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()