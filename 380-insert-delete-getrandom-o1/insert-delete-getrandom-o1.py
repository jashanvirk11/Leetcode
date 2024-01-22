class RandomizedSet:

    def __init__(self):
        # Initialize the data structures as needed
        self.value_to_index = {}  # Maps value to its index in the array
        self.values = []          # Stores the actual values

    def insert(self, val: int) -> bool:
        # Check if the value is already present
        if val in self.value_to_index:
            return False  # Value already exists, cannot insert

        # Add the value to the end of the list and update the map
        self.values.append(val)
        self.value_to_index[val] = len(self.values) - 1
        return True  # Successfully inserted

    def remove(self, val: int) -> bool:
        # Check if the value is present
        if val not in self.value_to_index:
            return False  # Value not found, cannot remove

        # Get the index of the value to be removed
        index = self.value_to_index[val]

        # Swap the value with the last element in the list
        self.values[index] = self.values[-1]
        self.value_to_index[self.values[-1]] = index

        # Remove the last element
        self.values.pop()
        del self.value_to_index[val]

        return True  # Successfully removed

    def getRandom(self) -> int:
        # Return a randomly selected value from the list
        random_index = random.randint(0, len(self.values) - 1)
        return self.values[random_index]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()