from program import Cache

memory_size = 2 ** 16 # mine
address_bits = 16 # mine
cache_size = 1024
block_size = 64
# blocks = 16
# sets = 4
associativity = 4
# tag length = 8
cache_type = "write_ack"

myCache = Cache(memory_size, address_bits, cache_size, block_size, associativity, cache_type)
