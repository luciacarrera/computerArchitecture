from ast import Num
from imp import cache_from_source
import math 
from Set import CacheSet

### CLASS Cache
class Cache:
    # function to initialize class instance
    def __init__(self, memory_size, memory_address, cache_size, block_size, associativity, cache_type):
        # set values to self
        self.memory_size = memory_size
        self.memory_address = memory_address
        self.cache_size = cache_size
        self.block_size = block_size
        self.associativity = associativity

        # check cache type is correct
        try:
            self.cache_type = self.check_type(cache_type)
        except AssertionError as msg:
            print(msg)
        else:

            # calculates number of blocks, sets
            self.num_blocks, self.num_sets = self.calculate()

            # calculates all the bits in memory address
            self.tag_bits, self.index_bits, self.offset_bits = self.bits()

            # creates sets
            self.create_sets()

            # prints characteristics
            self.print_characteristics()


    # function that creates sets
    def create_sets(self):
        num_sets = int(2 ** self.index_bits)
        set_list = {}
        for i in range(0, num_sets):
            set_list[i] = CacheSet(i, self.offset_bits)

        
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
        num_blocks = int(self.cache_size/self.block_size)
        num_sets = int(num_blocks/self.associativity)
        return num_blocks, num_sets

    # function that calculates the bits of each part of the address
    def bits(self):
        # bits of block offset is 2^n blocksize, we get k
        offset_bits = math.log2(self.num_blocks)

        # now we calculate number of sets
        index_bits = math.log2(self.num_sets)

        # bits of tag, tag = address_bits - index_bits - offset_bits
        tag_bits = self.memory_address - index_bits - offset_bits

        return tag_bits, index_bits, offset_bits


    # function that checks cache type
    def check_type(self, cache_type):
        # check if correctly written the type
        assert cache_type == "write_back" or cache_type == "read_back", 'Error: Cache Type not recognized'
        return cache_type

    def print_characteristics(self):
        print("-----------------------------------------")
        print("Memory size =", self.memory_size)
        print("Cache size =", self.cache_size)
        print("Block size =", self.block_size)
        print("Associativity =", self.associativity)
        print("Cache Type =", self.cache_type)
        print("Number of Blocks =", self.num_blocks)
        print("Number of Sets =", self.num_sets)
        print()
        print("Address length = ", self.memory_address)
        print("Tag length = ", self.tag_bits)
        print("Index length = ", self.index_bits)
        print("Offset length = ", self.offset_bits)
        print("-----------------------------------------\n")

