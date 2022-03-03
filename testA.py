from program import Simulator

memory_size = 2 ** 16 # mine
cache_size = 1024
block_size = 64
# blocks = 16
# sets = 4
associativity = 4
# tag length = 8
cache_type = "write_back"

mySimulator = Simulator(memory_size, cache_size, block_size, associativity, cache_type)
