x = 1
y = 2
buf = 0
total = 2
while(True):
    if ( y > 4000000 ):
        break
    buf = y
    y += x
    x = buf
    if y % 2 == 0:
        total += y

print total
    
