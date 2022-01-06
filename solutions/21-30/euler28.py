i = 1
dif = 2
j = 1

sum = 0
while i <= 1001**2:
    sum += i
    i += dif

    if j%4==0:
        dif += 2

    j += 1

print(sum)