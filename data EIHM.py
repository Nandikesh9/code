n=int(input())
data=["none" for i in range(n)]
for i in range(n):
    var=int(input())
    data[i]=var
data.pop(2)
print(data)
