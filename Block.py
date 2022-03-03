### CLASS cache block
class CacheBlock:
    def init(self, tag, clean, valid):
        self.tag = tag
        self.clean = clean  # boolean
        self.valid = valid  # boolean
        # bytearray of block size