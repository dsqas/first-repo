a = int(input())
for i in range(10):
    if i == a // 100:
        break
    for j in range(10):
        if j == a % 100 // 10:
            break
        for k in range(10):
            if k == a % 10:
                break

print(i, j, k, sep='')
