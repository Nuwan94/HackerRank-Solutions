from fractions import Fraction

x = [4, 3]
y = [5, 4]
z = [4, 4]

xRed = x[0] / sum(x) # Red Probability from X
yRed = y[0] / sum(y) # Red Probability from Y
zRed = z[0] / sum(z) # Red Probability from Z

prob = (xRed * yRed * (1 - zRed)) + (xRed * (1 - yRed) * zRed) + ((1 - xRed) * yRed * zRed)

print(Fraction(prob).limit_denominator())
