
import math
from operator import index
from Cache import Cache

'''#from torch import le
# global variable for memory (Bytearray)
block = [[],[]]
blocks = []

### MAIN FUNCTION
def main():
    memory_size = 2 ** 16
    address_bits = 16
    cache_size = 1024
    block_size = 64
    # blocks = 16
    # sets = 4
    associativity = 4
    # tag length = 8
    cache_type = "write_back"

    myCache = Cache(memory_size, address_bits, cache_size, block_size, associativity, cache_type)
    
    
    #mapping(myCache, 2000)
    tag, index, offset = mapping(myCache, 4616)
    word, tag1 = read_word(myCache, 46916)
    if (tag == tag1):
        print("read hit, the word is ", word)
    else:
        print("read miss")'''

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