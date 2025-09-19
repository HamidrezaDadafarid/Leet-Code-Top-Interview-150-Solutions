class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.list = []
        self.last_index = 0

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.list.append(val)
        self.map[val] = self.last_index
        self.last_index += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        index = self.map[val]
        last_val = self.list[-1]

        self.list[index] = last_val
        self.list.pop()

        self.map[last_val] = index
        del self.map[val]

        self.last_index -= 1

        return True

    def getRandom(self) -> int:
        return self.list[random.randint(0, self.last_index - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
