def reverseBit(n: int) -> int:
    res = 0 #000000
    for i in range(32):
        bit = (n >> i) & 1 # & 1 will pop the last bit
        res = (bit << (31 - i)) | res # | 0 will add bit
    return res

print(reverseBit(43261596)) # 964176192
print(reverseBit(1))
print(2**31)