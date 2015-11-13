num = 600851475143
prime = 3
n = num

while prime < n:
    if n % prime == 0:
        n = n/prime
    else:
        prime += 2

print n
