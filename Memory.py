## CLASS cache block
class Memory:
    def __init__(self, size):
        self.size = size
        self.memoryArray = bytearray(size)
    