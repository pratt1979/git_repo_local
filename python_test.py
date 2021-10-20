N=3
R=[2, 1, 0, 2] 
C=[0, 2, 1, 2]

loc=list(zip(R,C))
print(loc)

def findAdjacentCells(m,n,k):
    lst1=[]
    if m-1>=0:
        if n-1>=0:
            lst1.append((m-1,n-1))
        if n+1<=k:
            lst1.append((m-1,n+1))
    lst1.append((m-1,n))
    lst1.append((m,n))
    if n-1>=0:
        lst1.append((m,n-1))
    if n+1 <=k:
        lst1.append((m,n+1))
    if m+1<=k:
        if n-1>=0:
            lst1.append((m+1,n-1))            
        if n+1<=k:
            lst1.append((m+1,n+1))
    lst1.append((m+1,n))
    return lst1
        
        

k=N-1
for i in range(N):
    str1=""
    for j in range(N):
        loc1=(i,j)
        cnt=0
        if loc1 in loc:
            str1+="B"
        else:
            lst1=findAdjacentCells(i,j,N-1)
            for x in lst1:
                if x in loc:
                    cnt+=1
            str1+=str(cnt)
    print(str1)
    #new python code"