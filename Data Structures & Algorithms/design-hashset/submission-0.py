class MyHashSet:

    def __init__(self):
        self.arr = [0] * 1000001

    def add(self, key: int) -> None:
        self.arr[key] = 1

    def remove(self, key: int) -> None:
        self.arr[key] = 0

    def contains(self, key: int) -> bool:
        return self.arr[key] == 1