class Word:
    def __init__(self, address, address_bits, tag_bits, index_bits, offset_bits):
        self.address = address
        self.binary, self.tag, self.index, self.offset, self.range = self.mapping(address_bits, tag_bits, index_bits, offset_bits)

    def mapping(self,address_bits, tag_bits, index_bits, offset_bits):    
        # transform to binary
        binary = format(self.address, "b")
        # add additional zeroes to string
        binary= binary.zfill(address_bits)

        # get block offset and transform binary to integer
        end = address_bits
        start = address_bits - offset_bits
        offset = int(binary[start:end],2)

        # get index
        end = start
        start = end - index_bits
        index = int(binary[start:end],2)

        # get tag
        end = tag_bits
        start = 0
        tag = int(binary[start:end],2)
        
        # get range
        range0 = int(format(tag, "b") + format(index, "b") + "000000",2)
        range1 = int(format(tag, "b") + format(index, "b") + "111111",2)
        range = f"( {range0} - {range1} ]"
        return binary, tag, index, offset, range

