composites = []
total = 0
i = 2
n = 2000000

while(i <= n):
    if i not in composites:
        total += i
        print i
        j = i
        while(j <= n/i):
            composites.append(i*j)
            j += 1
    i += 1

print total
