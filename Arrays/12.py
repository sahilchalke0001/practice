380. Insert Delete GetRandom O(1)
import random

class RandomizedSet(object):

    def __init__(self):
        # List to store elements
        self.nums = []
        # Dictionary to store value -> index mapping
        self.pos = {}

    def insert(self, val):
        """
        Inserts a value to the set.
        Returns True if the set did not already contain the specified element.
        """
        if val in self.pos:
            return False
        # Add val at the end of list
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set.
        Returns True if the set contained the specified element.
        """
        if val not in self.pos:
            return False
        # Get index of element to remove
        idx = self.pos[val]
        # Move the last element to the place of the element to remove
        last_element = self.nums[-1]
        self.nums[idx] = last_element
        self.pos[last_element] = idx
        # Remove the last element
        self.nums.pop()
        del self.pos[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        """
        return random.choice(self.nums)

t-O(N)
s-O(1)