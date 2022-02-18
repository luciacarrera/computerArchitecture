import math
from operator import index
# global variable for memory (Bytearray)

### CLASS Cache
class Cache:

    # function to initialize class instance
    def __init__(self, memory_size, memory_address, cache_size, block_size, associativity, cache_type):
        self.memory_size = memory_size
        self.memory_address = memory_address
        self.cache_size = cache_size
        self.block_size = block_size
        self.associativity = associativity
        self.cache_type = cache_type
        # self.blocks[] = blocks[]
    
    # function that calculates the bits of each part of the address
    def bits(self):
        # bits of block offset is 2^n blocksize, we get k
        offset_bits = math.log2(self.block_size)

        # bits of block offset is 2^k sets, for that first we calculate number of blocks
        # num blocks = log2(cache size / block size)
        num_blocks = math.log2(self.cache_size/self.block_size)
        # now we calculate number of sets
        index_bits = num_blocks/self.associativity

        # bits of tag, tag = address_bits - index_bits - offset_bits
        tag_bits = self.memory_address - self.index_bits - self.offset_bits
        return tag_bits, offset_bits, index_bits

      
    

### CLASS cache set
class cache_set:
    def init(self, attribute):
        self.attribute = attribute  # placeholder


### CLASS cache block
class cache_block:
    def init(self, tag, clean, valid):
        self.tag = tag
        self.clean = clean  # boolean
        self.valid = valid  # boolean


### MAIN FUNCTION
def main():
    ## define simulator parameters
    # memory size in bits ?
    memory_size = 64000  # 64K

    # memory address in bits
    memory_address = 16

    # size of the cache, in bytes
    cache_size = 1024

    # size of a cache block, in bytes
    block_size = 64

    # associativity of the cache (direct-mapped = 1)
    associativity = 1

    # whether the cache is a write-back or write-through cache
    cache_type = "write-back"

    # call simulator function
    myCache = Cache(memory_size, memory_address, cache_size, block_size, associativity, cache_type)
    myCache.bits()

    #mapping (46916)





### FUNCTION to calculate address mapping, address in integer format
def mapping(address):
    # transform to binary
    binary = bin(address).replace("0b","")
    print(binary)

    # get block offset bits and find  block offset
    offset  = int(binary) % 100000
    offset = int(str(offset),2)
    print(offset)

    # get index bits and find index

    index = int(binary) % 10000000000
    index = int(index / 1000000)
    index = int(str(index),2)
    print(index)

    # get tag bits and find tag

    tag = int(int(binary) / 10000000000)
    tag = int(str(tag),2)
    print(tag)

    # get block index ?


### FUNCTION that returns the value read from the specified address an
def read_word(address):
    # check each address for four-bit alignment
    # check for range 0 ≤ address < memSize, where memSize is the number of bytes in the memory.
    word = ""
    process_word()
    return word


### FUNCTION that writes the provided word to the specified address.
def write_word(address, word):
    # check each address for four-bit alignment
    # check for range 0 ≤ address < memSize, where memSize is the number of bytes in the memory.
    word = ""
    process_word()


### FUNCTION that processes read and write as a single underlying function
def process_word():
    print()

    

### TESTING
main()
