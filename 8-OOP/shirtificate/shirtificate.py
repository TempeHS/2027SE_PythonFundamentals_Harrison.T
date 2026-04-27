    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("capacity must be a non-negative int")
            raise ValueError("Capacity cannot be less then 0")
        self._capacity = capacity
        self._size = 0

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("deposit amount must be a non-negative int")
            raise ValueError("deposit amount can't be a negative integer")
        if self._size + n > self._capacity:
            raise ValueError("too many cookies")
            raise ValueError("Too Many Cookies")
        self._size += n
    
    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("withdraw amount must be a non-negative int")
            raise ValueError("withdraw amount must not be a negative integer")
        if n > self._size:
            raise ValueError("not enough cookies")
            raise ValueError("Not Enough Cookies")
        self._size -= n