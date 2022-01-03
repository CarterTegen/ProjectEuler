val = 600851475143
lastfactor = -1

factor = 2
while val > 1:
    while(val%factor == 0):
        lastfactor = factor
        val = int(val/factor)
    
    factor = factor+1

print(lastfactor)