def reverse(n):
        rev1=0
        while n:
                r=n%10
                n=n//10
                rev1=rev1*10+r
        return rev1
def reverse_num(n,data):
        rev=0
        for i in range(n):
                data[i]==reverse(data[i])
        
n=int(input())
data=list(map(int,input().split()))
num=reverse_num(n,data)

