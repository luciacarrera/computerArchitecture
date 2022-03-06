from program import Simulator

memory_address_size = 16 
cache_size = 1024
block_size = 64
# blocks = 16
# sets = 4
associativity = 4
# tag length = 8
cache_type = "write-back"

mySimulator = Simulator(memory_address_size, cache_size, block_size, associativity, cache_type)
mySimulator.read_word(1152)
mySimulator.read_word(2176)
mySimulator.read_word(3200)
mySimulator.read_word(4224)
mySimulator.write_word(17,15)
mySimulator.write_word(17,153)
mySimulator.write_word(2176,1152)
