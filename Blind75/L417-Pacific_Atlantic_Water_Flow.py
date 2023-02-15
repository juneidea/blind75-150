#      pac
# pac  []  atl
#      atl
def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:
    ROWS, COLS = len(heights), len(heights[0])
    pac, atl = set(), set()

    def dfs(r, c, visit, prevHeight):
        if r not in range(ROWS) or c not in range(COLS) or (r, c) in visit or heights[r][c] < prevHeight:
            return
        visit.add((r, c))
        dfs(r+1, c, visit, heights[r][c])
        dfs(r-1, c, visit, heights[r][c])
        dfs(r, c+1, visit, heights[r][c])
        dfs(r, c-1, visit, heights[r][c])
        
    for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
    for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

    return pac.intersection(atl)

heights1 = [[1,2,2,3,5],
            [3,2,3,4,4],
            [2,4,5,3,1],
            [6,7,1,4,5],
            [5,1,1,2,4]]
print(pacificAtlantic(heights1))
