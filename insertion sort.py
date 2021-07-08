def insertionsort(n,data):
      for i in range(1,n):
            key=data[i]
            for j in range(i-1,-1,-1):
                  if key>data[j]:
                        data[j+1]=key
                        break
                  else:
                        data[j+1]=data[j]
                        j-=1
            else:
                  data[0]=key
            print(data)
n=int(input())
data=list(map(int,input().split()))
insertionsort(n,data)     
