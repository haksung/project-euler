composites = []
prime = []
i = 2
n = 600851475143
num = math.sqrt(n)

while(i <= num):
    if i not in composites:
        if n % i == 0:
            prime.append(i)
        j = i
        while(j <= num/i):
            composites.append(i*j)
            j += 1
    i += 1

print prime[len(prime)-1]
