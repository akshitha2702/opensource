N=int(input())
arr=[list(map(int,input().split()))for _ in range(N)]
for j in range(N):
    print(" ".join(str(arr[i][j]) for i in range(N)))
