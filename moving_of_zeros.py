def moveszeros(n,data):
      for i in range(n):
            if data[i]==0:
                  data.pop(i)
                  data.insert(len(data),0)
      return data
n=int(input())
data=list(map(int,input().split()))
zero=moveszeros(n,data)
print(*zero)
'''
10
1 0 2 0 20 30 2 4 0 5

5
1 0 2 3 4
'''
