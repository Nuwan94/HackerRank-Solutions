from statistics import median

n = int(input())
arr = [int(x) for x in input().split()]

arr.sort()

middle = int(len(arr) / 2)
lowerHalf = arr[:middle]
upperHalf = arr[middle:] if len(arr) % 2 == 0 else arr[middle + 1:]

print(int(median(lowerHalf)))
print(int(median(arr)))
print(int(median(upperHalf)))
