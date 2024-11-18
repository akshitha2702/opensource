N=int(input())
matrix=[]
for _ in range(N):
    matrix.append(list(map(int,input().split())))
row_sums=[sum(matrix[i]) for i in range(N)]
column_sums=[sum(matrix[j][i] for j in range(N)) for i in range(N)]
resultant=[]
for i in range(N):
    resultant.append(row_sums[i]+column_sums[i])
print(" ".join(map(str,resultant)))
