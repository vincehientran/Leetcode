from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.hashmap.move_to_end(key)   # update the k,v to be recent
            return self.hashmap[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap.move_to_end(key)   # update the k,v to be recent
        self.hashmap[key] = value
        
        if len(self.hashmap) > self.capacity:
            self.hashmap.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)