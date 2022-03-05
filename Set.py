from Block import CacheBlock
#from Cache import Cache
### CLASS cache set
class CacheSet:
    def __init__(self, index, associativity, block_size):
        # set the attributes
        self.index = index 
        self.associativity = associativity
        self.block_size = block_size
        self.tag_queue = [-1] * associativity # TODO

        # creates the blocks
        self.create_blocks()
    
    
    # function that creates sets
    def create_blocks(self):
        block_list = {}
        for i in range(0, self.associativity):
            block_list[i] = CacheBlock(i, self.block_size)