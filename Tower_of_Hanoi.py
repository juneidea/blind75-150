def towerOfHanoi1(n, fromRod, toRod, usingRod):
    if n == 1:
        print('Move disk 1 from', fromRod, 'to', toRod)
        return
    towerOfHanoi(n-1, fromRod, usingRod, toRod)
    print('Move disk', n, 'from', fromRod, 'to', toRod)
    towerOfHanoi(n-1, usingRod, toRod, fromRod)

# towerOfHanoi(3, 'A', 'C', 'B')

def towerOfHanoi(n, fromRod, toRod, usingRod):
    stacks = [[],[],[]]
    for i in range(n, 0, -1):
        stacks[0].append(i)
    print(stacks)
    def stackOfHanoi(n, fromRod, toRod, usingRod):
        if n == 1:
            moveFrom = stacks[fromRod].pop()
            stacks[toRod].append(moveFrom)
            print(stacks)
            return
        stackOfHanoi(n-1, fromRod, usingRod, toRod)
        moveFrom = stacks[fromRod].pop()
        stacks[toRod].append(moveFrom)
        print(stacks)
        stackOfHanoi(n-1, usingRod, toRod, fromRod)
    stackOfHanoi(n, fromRod, toRod, usingRod)

towerOfHanoi(3,0,2,1)