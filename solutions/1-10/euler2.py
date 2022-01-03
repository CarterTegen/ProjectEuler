v1 = 1
v2 = 2

sum = 0
while(max(v1,v2) < 4000000):
    if v1%2 == 0:
        sum += v1

    if v2%2 == 0:
        sum += v2
    
    v1 = v1 + v2
    v2 = v1 + v2

print(sum)