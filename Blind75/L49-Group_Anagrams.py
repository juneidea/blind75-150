from typing import DefaultDict
# Tuple Key O n*m, O n
def groupAnagrams1(strs: list[str]) -> list[list[str]]:
    res = DefaultDict(list)
    for s in strs:
        count = [0] * 26 # a...z
        for c in s:
            count[ord(c) - ord('a')] += 1
        # turn [] into tuple as a key
        res[tuple(count)].append(s)
    return res.values()
# Sorted Key O n*mlogm, O n
def groupAnagrams2(strs: list[str]) -> list[list[str]]:
    res = DefaultDict(list)
    for s in strs:
        key = "".join(sorted(s))
        # DefaultDict allow default [] for append
        res[key].append(s)
    return res.values()

str1 = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams1(str1))