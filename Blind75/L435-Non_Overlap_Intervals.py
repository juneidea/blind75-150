def overlapIntervals(intervals: list[list[int]]) -> int:
    intervals.sort(key = lambda v: v[0])
    count = 0
    prevEnd = intervals[0][1]
    for start, end in intervals[1:]:
        if start >= prevEnd:
            prevEnd = end
        else:
            count += 1
            prevEnd = min(end, prevEnd)
    return count

print(overlapIntervals([[1,2],[2,3],[3,4],[1,3]]))