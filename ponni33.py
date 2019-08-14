#p
a1=int(input())
a2=[]
for i in range(0,a1):
    a2.append(list(map(int,input().split())))
c=0
k=0
for i in range(0,a1):
   for j in range(0,a1):
        if a2[i][j]==1:
