def sum_of_nums(n,data):
    res=0
    for i in range(n):
            res+=data[i]
    return res
n=int(input())
data=list(map(int,input().split()))
total=sum_of_nums(n,data)
print(total)
