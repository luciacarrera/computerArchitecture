### CLASS cache block
from numpy import block


class CacheBlock:
    def __init__(self, index, block_size):
        self.size = block_size
        self.index = index
        self.blockArray = bytearray(block_size)

        '''self.tag = tag
        self.clean = clean  # boolean
        self.valid = valid  # boolean
        # bytearray of block size'''