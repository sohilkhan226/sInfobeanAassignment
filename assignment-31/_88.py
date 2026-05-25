# Q88: Rearrange a string so that identical characters are at least d distance apart.
# Input: S = "aaabc", d = 2
# Output: "abaca"
import heapq
from collections import Counter
S = "aaabc"
d = 2
freq = Counter(S)
heap = [(-count, char) for char, count in freq.items()]
heapq.heapify(heap)
result = []
wait_queue = []
while heap:
    count, char = heapq.heappop(heap)
    result.append(char)
    wait_queue.append((count + 1, char, len(result) + d - 1))
    if wait_queue and wait_queue[0][2] <= len(result):
        cnt, ch, _ = wait_queue.pop(0)
        if cnt < 0:
            heapq.heappush(heap, (cnt, ch))
if len(result) == len(S):
    print("".join(result))
else:
    print("Not possible")