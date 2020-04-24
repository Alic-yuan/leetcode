class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self._size = 0
        self.begin = 0
        self.last = 0
        self._capicaty = k
        self._data = [-1] * k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self._data[self.begin] = value
        else:
            self.begin = (self.begin - 1) % self._capicaty
            self._data[self.begin] = value
        self._size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self._data[self.last] = value
        else:
            self.last = (self.last + 1) % self._capicaty
            self._data[self.last] = value
        self._size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self._data[self.begin] = -1
        self.begin = (self.begin + 1) % self._capicaty
        self._size -= 1
        if self.isEmpty():
            self.last = self.begin
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self._data[self.last] = -1
        self.last = (self.last - 1) % self._capicaty
        self._size -= 1
        if self.isEmpty():
            self.begin = self.last
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self._data[self.begin]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self._data[self.last]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self._size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self._size == self._capicaty

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