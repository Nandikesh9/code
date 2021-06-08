def second_max(n,data):
      c=0
      s=max(data)
      c+=1
      if c==1:
            e=data.remove(s)
      e=max(data)
      for i in range(len(data)):
            print(i,data[i])
            if data[i]==max(data):
                  return i,e
      
n=int(input())
data=list(map(int,input().split()))
second=(second_max(n,data))
print(second)
