from fractions import Fraction
count = 0
for i in range(1, 7):
    for j in range(1, 7):
        if i != j and i + j == 6:
            count += 1
print(Fraction(count, 36))
