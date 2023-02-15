def encode(strs: list[str]) -> str:
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

def decode(str: str) -> list[str]:
    res, i = [], 0
    while i < len(str):
        j = i
        while str[j] != "#":
            j += 1
        length = int(str[i:j])
        res.append(str[j+1:j+length+1])
        i = j+length+1
    return res



strs1 = ["leetcodelove", "leet", "code", "love"]
print(encode(strs1)) # 12#leetcodelove4#leet4#code4#love
print(decode(encode(strs1)))