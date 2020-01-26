N, M = map(lambda x: int(x), input().split())
array = list(map(lambda x: int(x), input().split()))
queries = []
for _ in range(M):
    queries.append(list(map(lambda x: int(x), input().split())))
# print(N, M, array, queries)
print(len(queries), queries[0], queries[0][1])
for i in len(queries):
    inrange = [m for m in array if m >= queries[0] and m <= queries[1]]
    multiply = reduce((lambda x, y: x * y), inrange)
    F

