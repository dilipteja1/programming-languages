import heapq

'''
T1 - 10
T2 - 4
T3 - 8
T4- 1
T5 - 2

'''

data = [10, 4, 8, 1, 2]

# priority queue
heapq.heapify(data)
print(data)

print(heapq.heappop(data))

