### MAIN FUNCTION
def main():
    # define simulator parameters

    # size of memory address in bits
    memory_address = 16

    # size of the cache, in bytes
    cache_size = 0

    # size of a cache block, in bytes
    block_size = 0

    # associativity of the cache
    associativity = 4

    # whether the cache is a write-back or write-through cache
    cache_type = "write-back"

    # call simulator function
    simulator(memory_address, cache_size, block_size, associativity, cache_type)



### FUNCTION that will stablish the cache size, block size, etc
def simulator(memory_address, cache_size, block_size, associativity, cache_type):
    print("here")



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