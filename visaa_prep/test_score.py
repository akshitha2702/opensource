N,X,Y=map(int,input().split())
if 0<=Y<=N*X and Y%X==0:
    print("YES")
else:
    print("NO")
