T=int(input())
for _ in range(T):
    X,Y=map(int,input().split())
    remaining=X-Y+1
    print(remaining)
