composites = []
index = 0
i = 2
n = 150000
while(True):
    if i not in composites:
        index += 1
        if index == 10001:
            print i
            break
        j = i
        while(j <= n/i):
            composites.append(i*j)
            j += 1
    i += 1
