## CLASS cache block
import random as rand


class Memory:
    def __init__(self, size):
        self.size = size
        self.memoryArray = []
        for i in range (size):
            rand_int = rand.randint(0, 256)
            self.memoryArray.append(bytearray(rand_int))