import itertools

def is_palindrome(num):
    s = str(num)
    return s == s[::-1]

z = itertools.combinations(range(999,554,-1), 2)
r = []
for x in z:
    s = x[0] * x[1]
    if is_palindrome(s):
        r.append(s)

print sorted(r, reverse=True)[0]
