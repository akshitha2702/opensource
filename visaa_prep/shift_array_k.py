n=int(input())
arr=list(map(int,input().split()))
k=int(input())
k=k%n
array=arr[-k:]+arr[:-k]
print(*array)
