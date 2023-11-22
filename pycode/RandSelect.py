'''
Implement a class RandSelector with 3 methods
add, remove, and select
add/remove func add/remove elements to the class
select method random select an element based on the past add/removes
All operations must be in constant time
C = RandSelector()
C.add(1)
C.add(3)
C.add(1)
C.add(3)
C.remove(3)
C.add(4)

C.select() --> 0.5 chance of 1, 0.25 chance of 3, 0.25 chance of 4
'''

import random
from collections import defaultdict

class RandSelector():
    def __init__(self):
        self.num_array = []
        self.index_map = defaultdict(set)

    
    def add(self,num):
        self.num_array.append(num)
        self.index_map[num].add(len(self.num_array) - 1)
    
    def remove(self,num):
        if num not in self.index_map:
            raise Exception('removing element that is not in index map')
        removal_index = self.index_map[num].pop()
        # swap and pop
        self.num_array[-1],self.num_array[removal_index] = self.num_array[removal_index], self.num_array[-1]
        self.num_array.pop()
    
    def select(self):
        return random.choice(self.num_array)


C = RandSelector()
C.add(1)
C.add(3)
C.add(3)
C.add(1)
C.remove(3)
print(C.select())