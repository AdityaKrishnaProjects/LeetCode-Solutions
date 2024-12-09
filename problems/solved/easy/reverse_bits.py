# one liner
# def reverseBits(n):
#     """
#     takes int
#     returns int (reversed bits)
#     """

#     return int((bin(n)[:1:-1] + "0"*(34-len(bin(n)))),2)

# print(reverseBits(43261596))
# print(reverseBits(4294967293))

# more bit manip logic (assumes they will actually give binary representations)
def reverseBits(n):
    """
    takes int
    returns int (reversed bits)
    """

    r_int = 0
    # processes exactly 32 bits
    for _ in range(32):  
        # records LSB in r_int (no left shift occurs at first iteration as 
        # 0 << 1 = 0)
        r_int = (r_int << 1) ^ (n & 1)  
        # processes next bit in r
        n >>= 1                     
    return r_int 

print(reverseBits(43261596))
print(reverseBits(4294967293))