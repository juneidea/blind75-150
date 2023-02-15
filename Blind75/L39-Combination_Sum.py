def combinationSum(candidates: list[int], target: int) -> list[int]:
    res = []
    
    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > target:
            return

        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        # complete the include before exclude is a must
        cur.pop()
        # not increase total until pass the if cond
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res

cans1 = [2,3,6,7]
target1 = 7
print(combinationSum(cans1, target1)) # [[2, 2, 3], [7]]