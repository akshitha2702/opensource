N=int(input())
sticks=list(map(int,input().split()))
sticks.sort(reverse=True)
perimeter=-1
for i in range(N-2):
    if sticks[i]<sticks[i+1]+sticks[i+2]:
        perimeter=sticks[i]+sticks[i+1]+sticks[i+2]
        break
print(perimeter)
