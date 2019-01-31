import statistics

n = int(input())
arr = [int(x) for x in input().split()]

print(statistics.mean(arr))
print(statistics.median(arr))

try:
    print(statistics.mode(arr))
except statistics.StatisticsError as e:
    d = {x: arr.count(x) for x in arr}
    modes = []
    for i in d.keys():
        if d[i] == max(d.values()):
            modes.append(i)
    print(sorted(modes)[0])
