class Hash:
    def __init__(self):
        self.capacity = 10
        self.map = [None] * self.capacity

    # Creates a hash value
    # Time complexity: O(1)
    def get_hash(self, key):
        return key % self.capacity

    # Inserts a value into the hash
    # Time complexity: O(1)
    def insert(self, key, value):
        key_hash = self.get_hash(key)
        kvp = [key, value]  # Key value pair
        # If self.map is empty, add item
        if self.map[key_hash] is None:
            self.map[key_hash] = list([kvp])
            return True
        # If an item exists already, add it to the map as well
        else:
            for items in self.map[key_hash]:
                if items[0] == key:
                    # Item is added
                    items[1] = value
                    return True
            self.map[key_hash].append(kvp)
            return True

    # Searches for a item in the hash
    # Time complexity: O(1)
    def search(self, key):
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
            # If the item exists, return it
            for items in self.map[key_hash]:
                if items[0] == key:
                    return items[1]
        # If item does not exist, return nothing
        return None
