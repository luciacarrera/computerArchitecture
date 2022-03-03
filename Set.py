from Block import CacheBlock
# from Cache import bits
### CLASS cache set
class CacheSet:
    def __init__(self, index, bits):
        self.index = index 
        self.bits = bits
        self.offset_bits = bits

    
    # function that creates sets
    def create_blocks(self):
        num_sets = 2 ** self.index_bits
        for i in range(0, num_sets):
            C(i)