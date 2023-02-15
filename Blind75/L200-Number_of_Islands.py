import collections
# Iterative
def numIslands(grid: list[list[str]]) -> int:
    if not grid: return 0
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    islands = 0

    def bfs(r, c):
        q = collections.deque()
        visit.add((r, c))
        q.append((r, c))

        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r in range(ROWS) and c in range(COLS) and grid[r][c] == "1" and (r, c) not in visit:
                    q.append((r, c))
                    visit.add((r, c))


    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1" and (r, c) not in visit:
                bfs(r, c)
                islands += 1
    return islands

# Recursive
def numIslands1(grid: list[list[str]]) -> int:
    if not grid: return 0
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    islands = 0

    def explore(r, c):
        if r not in range(ROWS) or c not in range(COLS) or grid[r][c] != "1" or (r, c) in visit:
            return False
        visit.add((r, c))
        # the other 4 just to collect visit T/F not matter
        explore(r + 1, c)
        explore(r - 1, c)
        explore(r, c + 1)
        explore(r, c - 1)

        return  True

    for r in range(ROWS):
        for c in range(COLS):
            if explore(r, c) == True:
                islands += 1
    return islands

grid1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(numIslands1(grid1)) #1
grid2 = [["1","1","1","0","0"],["1","1","0","0","0"],["1","1","0","0","0"],["0","0","0","1","1"]]
print(numIslands1(grid2)) #2

