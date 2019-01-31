from statistics import median

n = int(input())
arr = [int(x) for x in input().split()]
freq = [int(y) for y in input().split()]

arrNew = []

for a in range(len(freq)):
    for i in range(freq[a]):
        arrNew.append(arr[a])

arrNew.sort()

middle = int(len(arrNew) / 2)
lowerHalf = arrNew[:middle]
upperHalf = arrNew[middle:] if len(arrNew) % 2 == 0 else arrNew[middle + 1:]

print(float(median(upperHalf) - median(lowerHalf)))
