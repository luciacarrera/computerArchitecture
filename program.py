
import math
from operator import index
from Cache import Cache
from Memory import Memory

'''#from torch import le
# global variable for memory (Bytearray)
block = [[],[]]
blocks = []

### MAIN FUNCTION
def main():
    #mapping(myCache, 2000)
    tag, index, offset = mapping(myCache, 4616)
    word, tag1 = read_word(myCache, 46916)
    if (tag == tag1):
        print("read hit, the word is ", word)
    else:
        print("read miss")'''

class Simulator:
    def __init__(self, memory_size, address_bits, cache_size, block_size, associativity, type):
        self.address_bits = address_bits
        # create memory
        self.memory = Memory(memory_size)
        # create cache
        self.cache = Cache(cache_size, block_size, associativity, type)
        self.tag_bits, self.index_bits, self.offset_bits = self.calculate_bits()

        # prints characteristics
        self.print_characteristics()
    
    def print_characteristics(self):
        print("-----------------------------------------")
        print("Memory size =", self.memory.size)
        print("Cache size =", self.cache.size)
        print("Block size =", self.cache.block_size)
        print("Associativity =", self.cache.associativity)
        print("Cache Type =", self.cache.type)
        print("Number of Blocks =", self.cache.num_blocks)
        print("Number of Sets =", self.cache.num_sets)
        print()
        print("Address length = ", self.address_bits)
        print("Tag length = ", self.tag_bits)
        print("Index length = ", self.index_bits)
        print("Offset length = ", self.offset_bits)
        print("-----------------------------------------\n")

    # function that calculates the bits of each part of the address
    def calculate_bits(self):
        # bits of block offset is 2^n blocksize, we get k
        offset_bits = math.log2(self.cache.num_blocks)

        # now we calculate number of sets
        index_bits = math.log2(self.cache.num_sets)

        # bits of tag, tag = address_bits - index_bits - offset_bits
        tag_bits = self.address_bits - index_bits - offset_bits

        return tag_bits, index_bits, offset_bits


### FUNCTION to calculate address mapping, address in integer format
def mapping(cache, address):    
    # get bits from cache
    length = cache.memory_address
    tag_bits, index_bits, offset_bits = cache.bits()

    # transform to binary
    binary = format(address, "b")
    # add additional zeroes to string
    binary= binary.zfill(length)

    # get block offset and transform binary to integer
    end = length
    start = length - offset_bits
    offset = int(binary[start:end],2)

    # get index
    end = start
    start = end - index_bits
    index = int(binary[start:end],2)

    # get tag
    end = tag_bits
    start = 0
    tag = int(binary[start:end],2)

    range0 = int(format(tag, "b") + format(index, "b") + "000000",2)
    range1 = int(format(tag, "b") + format(index, "b") + "111111",2)
    print("Address:",address,"Binary:",binary, "Tag:", tag, "; Index:",index, "; Offest:",offset, "[", range0, "-", range1, "]")
    return tag, index, offset


### FUNCTION that returns the value read from the specified address an
def read_word(my_cache, address):
    # check each address for four-bit alignment
    # check for range 0 ≤ address < memSize, where memSize is the number of bytes in the memory.
    tag, index, offset = mapping(my_cache, address)
    #word = blocks[index][offset]
    #process_word()
    #return word, tag


### FUNCTION that writes the provided word to the specified address.
def write_word(address, word):
    # check each address for four-bit alignment
    # check for range 0 ≤ address < memSize, where memSize is the number of bytes in the memory.
    word = ""
    process_word()


### FUNCTION that processes read and write as a single underlying function
def process_word():
    print()

'''    
### TESTING
main()
'''