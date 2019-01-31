N = int(input())
X = [int(x) for x in input().split()]
W = [int(w) for w in input().split()]

sums = 0
for i in range(N):
    sums += (X[i] * W[i])

print(round(sums / sum(W), 1))
