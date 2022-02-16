# global variable for memory (Bytearray)

### CLASS cache
class cache:
    def init(self, attribute):
        self.attribute = attribute  # placeholder
        # self.blocks[] = blocks[]


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
    block_size = 1024

    # associativity of the cache (direct-mapped = 1)
    associativity = 1

    # whether the cache is a write-back or write-through cache
    cache_type = "write-back"

    # call simulator function
    simulator(memory_size, memory_address, cache_size, block_size, associativity, cache_type)

    mapping (46916)


### FUNCTION that will stablish the cache size, block size, etc
def simulator(memory_size, memory_address, cache_size, block_size, associativity, cache_type):
    print("here")


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
