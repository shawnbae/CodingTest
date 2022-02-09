N = int(input())

n = N // 10
q = N % 10

count = 0
while True:
    temp = 10 * (q) + ((n+q) %10)
    n, q = temp // 10, temp % 10
    count += 1

    if temp == N:
        break

print(count)