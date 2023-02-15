# L57
# def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:


# print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])) #[[1,2],[3,10],[12,16]]



# L56
# connect = merge too
# def merge(intervals: list[list[int]]) -> list[list[int]]:

# print(merge([[1,3],[8,10],[15,18],[2,6]])) # [[1, 6], [8, 10], [15, 18]]



# L435
# how many interval need to remove to make non overlap
# def overlapIntervals(intervals: list[list[int]]) -> int:

# print(overlapIntervals([[1,2],[2,3],[3,4],[1,3]])) # 1



# L252
class Interval(object):
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

# def meetingPossible(intervals: list[Interval]) -> bool:

# print(meetingPossible([Interval(0, 30), Interval(5, 10), Interval(15, 20)])) # False
# print(meetingPossible([Interval(0, 5), Interval(5, 10), Interval(15, 20)])) # True



# L253
# def meetingOverlap(intervals: list[Interval]) -> int:

# print(meetingOverlap([Interval(0, 30), Interval(5, 10), Interval(10, 20), Interval(15, 25)])) # 3



# L48
# def rotate(matrix: list[list[int]]) -> None:

matrix1 = [ [5,1,9,11],
            [2,4,8,10],
            [13,3,6,7],
            [15,14,12,16]]
# rotate(matrix1)
# print(matrix1) # [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]



# L54
# def spiralOrder(matrix: list[list[int]]) -> list[int]:

matrix2 = [ [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]]
# print(spiralOrder(matrix2)) # [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]



# L73
# def setZeros(matrix: list[list[int]]) -> None:

matrix3 = [ [1,0,1,1],
            [1,0,1,1],
            [1,1,1,1],
            [0,1,0,1]]
# setZeros(matrix3)
# print(matrix3)