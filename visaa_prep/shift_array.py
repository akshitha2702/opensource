N=int(input())
arr=list(map(int,input().split()))
sorted=arr[1:]+[arr[0]]
print(" ".join(map(str,sorted)))
