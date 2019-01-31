import statistics

n = int(input())
arr = [int(x) for x in input().split()]

print(round(statistics.pstdev(arr), 1))
