"""Note: Python collections module already have Dequeue."""


class Empty(Exception):
    """Returns Error if Dequeue is Empty."""
    pass


class Dequeue:
    """Class for Double Ended Queues."""
    default_capacity = 10                                             # Static Variable

    def __init__(self):
        self._data = [None] * Dequeue.default_capacity
        self._size = 0
        self._front = 0

    def __len__(self):                                                # Method Overloading
        """Returns number of elements in the dequeue."""
        return self._size

    def is_empty(self):
        """Check if Dequeue is empty."""
        return self._size == 0

    def first(self):
        """Returns first element of Dequeue."""
        if self.is_empty():
            return Empty("Dequeue is Empty.")

        return self._data[self._front]

    def last(self):
        """Returns last element of the Dequeue."""
        if self.is_empty():
            return Empty("Dequeue is Empty.")

        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def delete_first(self):
        """Removes and returns first element of the Dequeue."""
        if self.is_empty():
            return Empty("Dequeue is Empty.")

        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return answer

    def delete_last(self):
        """Removes and returns last element of the Dequeue."""
        if self.is_empty():
            return Empty("Dequeue is Empty.")

        back = (self._front + self._size) % len(self._data)
        answer = self._data[back]
        self._data[back] = None
        self._size -= 1

        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return answer

    def add_first(self, e):
        """Adds element at the start of the Dequeue."""
        if self._size == len(self._data):
            self._resize(len(self._data) * 2)

        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def add_last(self, e):
        """Adds element at the end of the Dequeue."""
        if self._size == len(self._data):
            self._resize(len(self._data) * 2)

        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        """To increase the size of the Dequeue"""
        old = self._data
        walk = self._front
        self._data = [None] * cap

        for i in range(len(self._data)):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)

        self._front = 0
