'''
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
'''

'''
超过69.18%
'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []
        self.len = 0
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.list.append(x)
        self.len += 1
        if self.min == None:
            self.min = x
        if self.min > x :
            self.min = x

    def pop(self):
        """
        :rtype: void
        """
        if self.len == 0:
            return False
        prev = self.list[-1]
        self.list.pop(self.len-1)
        self.len -= 1
        if prev == self.min:
            if self.list == []:
                self.min = None
            else:
                self.min = min(self.list)


    def top(self):
        """
        :rtype: int
        """
        return self.list[self.len-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
