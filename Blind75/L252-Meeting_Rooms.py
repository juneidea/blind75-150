class Interval(object):
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

def meetingPossible(intervals: list[Interval]) -> bool:
    intervals.sort(key = lambda i: i.start)
    for i in range(1, len(intervals)):
        i1 = intervals[i-1]
        i2 = intervals[i]
        if i1.end > i2.start:
            return False
    return True

print(meetingPossible([Interval(0, 30), Interval(5, 10), Interval(15, 20)])) # False
print(meetingPossible([Interval(0, 5), Interval(5, 10), Interval(15, 20)])) # True