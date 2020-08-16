class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.cap = k + 1
        self.arr = [0] * self.cap
        self.front = 0
        self.rear = 0

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.cap
        self.arr[self.front] = value
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.arr[self.rear] = value
        self.rear = (self.rear + 1) % self.cap
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.cap
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.cap
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def getRear(self):
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.arr[(self.rear - 1) % self.cap]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        """
        return self.front == self.rear

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        """
        return (self.rear + 1) % self.cap == self.front
