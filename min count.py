def minmax(n,data):
        s=data[0]
        for i in range(n):
                if s<i:
                        print(i,data[i],end=' ')
        return s
n=int(input())
data=list(map(int,input().split()))
s1=minmax(n,data)
print(s1)                
