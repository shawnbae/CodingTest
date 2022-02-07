import sys

T = int(input())
data = []
for _ in range(T):
    data.append(list(map(int, sys.stdin.readline().split())))
        
def factorial(n):
    res = 1
    for i in range(1, n+1):
        res*=i
    return res
    
for d in data:
    print(factorial(d[1])//(factorial(d[0]) * (factorial(d[1]-d[0]))))