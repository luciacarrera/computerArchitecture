from numpy import take_along_axis
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
        print(self.tag_queue)
        self.block_list = []
        self.block_index = -1

        # creates the blocks
        self.create_blocks()
    
    # function that creates the blocks
    def create_blocks(self):
        for i in range(0, self.associativity):
            self.block_list.append(CacheBlock(i, self.block_size))
    
    # function that adds the word
    def read_word(self, word):
        hit = False
        replace = False

        # check if tag is in queue
        for tag in self.tag_queue:
            if tag == word.tag:
                hit = True
                temp = self.tag_queue.pop(0)
                self.tag_queue.append(temp)
        
        if hit == False:
            # pop first value
            popped_tag = self.tag_queue.pop(0)

            # see if it's a replace
            if popped_tag == -1:
                replace = True

            # append word
            self.tag_queue.append(word.tag)
        
        # set the block index
        self.block_index += 1
        if self.block_index == self.associativity:
            self.block_index = 0

        ## ADD TO BLOCK

        
        "// addr=",word.address,"index=", word.index, "tag=",word.tag, word.range
        ## PRINT RESULTS
        myStr = "read "
        if hit:
            myStr += "hit"
        else: 
            myStr += "miss"

        print(self.tag_queue)
        print(self.block_index)