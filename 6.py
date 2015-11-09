sum_square = 0
square_sum = 0

for x in range(1,101):
    square_sum += x**2
    sum_square += x

sum_square = sum_square**2

print sum_square - square_sum
