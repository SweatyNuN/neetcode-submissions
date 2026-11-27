class MyHashSet:

    load: int
    buckets: list[list[int]]

    def __init__(self):
        self.load = 10
        self.buckets = [[] for _ in range(self.load)]

    def add(self, key: int) -> None:
        bucket = key % self.load
        if key not in self.buckets[bucket]:
            self.buckets[bucket].append(key)

    def remove(self, key: int) -> None:
        bucket = key % self.load
        if key in self.buckets[bucket]:
            self.buckets[bucket].remove(key)

    def contains(self, key: int) -> bool:
        bucket = key % self.load
        if key in self.buckets[bucket]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)