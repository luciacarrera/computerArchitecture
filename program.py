
import math
from operator import index

#from torch import le
# global variable for memory (Bytearray)
block = [[],[]]
blocks = []
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

        print("Memory size:", memory_size)
        print("Cache size:", cache_size)
        print("Block Size:", block_size)
        print("Associativity:", associativity)
        print("Cache Type:", cache_type, "\n\n")

        num_blocks = int(cache_size/block_size)
        for i in range(int(block_size/4)):
            block.append([bytearray(4),-1])
        for i in range(num_blocks):
            blocks.append(block.copy())
        arr = [45,12,3,7]
        #blocks[13][4] = [bytearray(arr),45]                    #DELETE

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
        tag_bits = self.memory_address - index_bits - offset_bits
        return int(tag_bits), int(index_bits), int(offset_bits)

      
    

### CLASS cache set
class CacheSet:
    def init(self, attribute):
        self.attribute = attribute  # placeholder


### CLASS cache block
class CacheBlock:
    def init(self, tag, clean, valid):
        self.tag = tag
        self.clean = clean  # boolean
        self.valid = valid  # boolean
        

### MAIN FUNCTION
def main():
    ## define simulator parameters
    # memory size in bits ?
    memory_size = 65536  # 64K

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
    
    
    #mapping(myCache, 2000)
    tag, index, offset = mapping(myCache, 4616)
    word, tag1 = read_word(myCache, 46916)
    if (tag == tag1):
        print("read hit, the word is ", word)
    else:
        print("read miss")
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
    word = process_word(index,offset)
    return word, tag


### FUNCTION that writes the provided word to the specified address.
def write_word(address, word):
    # check each address for four-bit alignment
    # check for range 0 ≤ address < memSize, where memSize is the number of bytes in the memory.
    word = ""



### FUNCTION that processes read and write as a single underlying function
def process_word(index,offset):
    arr, tag = blocks[index][offset]
    arr = list(arr)
    word = arr[0] + 256 * (arr[1] + 256 * (arr[2] + 256 * arr[3]))
    return word

    

### TESTING
main()
