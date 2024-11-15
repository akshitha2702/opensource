N=int(input())
for _ in range(N):
    print(*input().split()[::-1])
