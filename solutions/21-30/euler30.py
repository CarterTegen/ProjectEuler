
total_sum = 0
k = 5
for i in range(2, 354294):
    val = i

    sum = 0
    while val >= 1:
        digit = val % 10
        sum += digit ** k

        val = val // 10

    if sum == i:
        total_sum += sum

print(total_sum)
    