def reverse(n):
        rev1=0
        while n:
                r=n%10
                n=n//10
                rev1=rev1*10+r
        return rev1
def reverse_num(n,data):
        c=0
        for i in range(n):
                if data[i]==reverse(data[i]):
                        c+=1
        return c
        
n=int(input())
data=list(map(int,input().split()))
num1=reverse_num(n,data)
print(num1)
