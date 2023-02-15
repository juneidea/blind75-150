class Interval(object):
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

def meetingOverlap(intervals: list[Interval]) -> int:
    start = sorted([i.start for i in intervals ])
    end = sorted([i.end for i in intervals])
    lap, maxLap = 0, 0
    s, e = 0, 0

    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            lap += 1
            maxLap = max(maxLap, lap)
        else:
            e += 1
            lap -= 1
        
    return maxLap
print(meetingOverlap([Interval(0, 30), Interval(5, 10), Interval(10, 20), Interval(15, 25)])) # 3