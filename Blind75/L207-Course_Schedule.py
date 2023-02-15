def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    preMap = { i:[] for i in range(numCourses)}
    for pre, crs in prerequisites:
        preMap[pre].append(crs)

    visited = set()
    def dfs(pre):
        # loop crs can not finish
        if pre in visited:
            return False
        if not preMap[pre]:
            return True
        # getting False is end getting True is continue
        visited.add(pre)
        for crs in preMap[pre]:
            if not dfs(crs):
                return False
        # cleaning up for loop below repeating use of these two
        visited.remove(pre)
        preMap[pre] = []
        return True
    # test False in all node because graph may not all connected
    # if graph = connected => after 0 preMap will be empty then dfs just do a boring add remove
    for pre in range(numCourses):
        if not dfs(pre):
            return False
    return True

num1, preReq1 = 5, [[0,1],[0,2],[1,3],[1,4],[3,4]]
num2, preReq2 = 3, [[0,1],[1,2],[2,0]]
print(canFinish(num1, preReq1)) # True
print(canFinish(num2, preReq2)) # False
