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
        self.block_list = []

        # creates the blocks
        self.create_blocks()
    
    
    # function that creates sets
    def create_blocks(self):
        for i in range(0, self.associativity):
            self.block_list.append(CacheBlock(i, self.block_size))