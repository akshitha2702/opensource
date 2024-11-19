n=int(input())
heights=list(map(int,input().split()))
current_altitude=0
max_altitude=0
for height in heights:
    current_altitude+=height
    max_altitude=max(max_altitude,current_altitude)
print(max_altitude)
