a = int(input())
b = a % 1000
i = j = k = 0
for i in range(10):
    if i == b // 100 :
        break
    for j in range(10):
        if j == b % 100 // 10:
            break
        for k in range(10):
            if k == b % 10:
                 break
print(i, j, k, sep=' ')
