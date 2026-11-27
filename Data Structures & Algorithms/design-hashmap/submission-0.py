class MyHashMap:

    load: int
    buckets: list[list[tuple[int, int]]]

    def __init__(self):
        self.load = 10
        self.buckets = [[] for _ in range(self.load)]

    def put(self, key: int, value: int) -> None:
        bucket = key % self.load
        for index, element in enumerate(self.buckets[bucket]):
            if element[0] == key:
                self.buckets[bucket][index] = (key, value)
                return
        self.buckets[bucket].append((key, value))

    def get(self, key: int) -> int:
        bucket = key % self.load
        for element in self.buckets[bucket]:
            if element[0] == key:
                return element[1]
        return -1

    def remove(self, key: int) -> None:
        bucket = key % self.load
        for index, element in enumerate(self.buckets[bucket]):
            if element[0] == key:
                del self.buckets[bucket][index]
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)