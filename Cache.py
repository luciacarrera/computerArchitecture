from ast import Num
import math 
from Set import CacheSet

### CLASS Cache
class Cache:
    # function to initialize class instance
    def __init__(self, size, block_size, associativity, cache_type):
        # set values to self
        #self.address_bits = address_bits
        self.size = size
        self.block_size = block_size
        self.associativity = associativity
        # calculates number of blocks, sets
        self.num_blocks, self.num_sets = self.calculate()

        # creates sets
        self.create_sets()

        # check cache type is correct
        try:
            self.type = self.check_type(cache_type)
        except AssertionError as msg:
            print(msg)
       

    # function that creates sets
    def create_sets(self):
        set_list = {}
        for i in range(0, self.num_sets):
            set_list[i] = CacheSet(i, self.associativity, self.block_size)

        
    '''
        num_blocks = int(cache_size/block_size)
        for i in range(int(block_size/4)):
            block.append([bytearray(4),-1])
        for i in range(num_blocks):
            blocks.append(block.copy())
        arr = [45,12,3,7]
        blocks[13][4] = [bytearray(arr),45]'''

    # function that calculates number of sets, blocks, etc
    def calculate(self):
        num_blocks = int(self.size/self.block_size)
        num_sets = int(num_blocks/self.associativity)
        return num_blocks, num_sets

    # function that checks cache type
    def check_type(self, cache_type):
        # check if correctly written the type
        assert cache_type == "write-back" or cache_type == "write-through", 'Error: Cache Type not recognized\n'
        return cache_type

