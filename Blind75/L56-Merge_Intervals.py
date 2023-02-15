def merge(intervals: list[list[int]]) -> list[list[int]]:
    # sort is O logn
    intervals.sort(key = lambda v: v[0])
    output = [intervals[0]]
    for start, end in intervals[1:]:
        if output[-1][1] >= start:
            output[-1][1] = max(end, output[-1][1])
        else:
            output.append([start, end])
    return output

print(merge([[1,3],[8,10],[15,18],[2,6]])) # [[1, 6], [8, 10], [15, 18]]