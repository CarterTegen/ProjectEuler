ans = 1
n = 20
for i in range(1, n + 1):

    if ans % i != 0:
        for j in range(1, i + 1):
            if (ans * j) % i == 0:
                ans = ans * j
                break


print(ans)
