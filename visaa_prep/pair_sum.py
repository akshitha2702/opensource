N=int(input())
arr=list(map(int,input().split()))
K=int(input())
for i in range(N):
    for j in range(i+1,N):
        if arr[i]+arr[j]==K:
            print("true")
            exit()

print("false")
