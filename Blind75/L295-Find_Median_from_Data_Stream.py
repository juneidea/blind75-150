import heapq
class MedianFinder:
    def __init__(self):
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # python only have min heap
        heapq.heappush(self.small, -1 * num)

        # make sure every num small is <= every num in large
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # uneven size
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
    
    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        elif len(self.small) > len(self.large):
            return -1 * self.small[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2
            

stream1 = MedianFinder()
stream1.addNum(3)
stream1.addNum(2)
print(stream1.findMedian()) # 2.5
stream1.addNum(7)
print(stream1.findMedian()) # 3
stream1.addNum(4)
print(stream1.findMedian()) # 3.5