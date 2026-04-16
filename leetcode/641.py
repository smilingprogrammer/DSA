class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.dq = deque()
        

    def insertFront(self, value: int) -> bool:
        curr_len = len(self.dq)
        if curr_len == self.k:
            return False
        self.dq.appendleft(value)

        if curr_len != len(self.dq):
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        curr_len = len(self.dq)
        if curr_len == self.k:
            return False
        self.dq.append(value)
        if curr_len != len(self.dq):
            return True
        else:
            return False
        

    def deleteFront(self) -> bool:
        curr_len = len(self.dq)
        if self.dq:
            self.dq.popleft()
        if curr_len != len(self.dq):
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        curr_len = len(self.dq)
        if self.dq:
            self.dq.pop()
        if curr_len != len(self.dq):
            return True
        else:
            return False

    def getFront(self) -> int:

        if self.dq:
            return self.dq[0]
        else:
            return -1
        

    def getRear(self) -> int:
        if self.dq:
            return self.dq[-1]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if self.dq:
            return False
        else:
            return True

    def isFull(self) -> bool:
        if len(self.dq) == self.k:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()