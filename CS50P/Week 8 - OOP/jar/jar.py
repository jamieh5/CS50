class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        return "🍪" * self.size

    def deposit(self, num):
        if self._size + num <= self._capacity:
            self._size += num
        else:
            raise ValueError

    def withdraw(self, num):
        if self._size - num >= 0:
            self._size -= num
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar()
    jar.deposit(12)
    print(str(jar))
if __name__ == "__main__":
    main()
