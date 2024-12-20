class MyHashSet:
    def __init__(self):
        self.hashset=[]

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashset.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key): self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        return True if key in self.hashset else False