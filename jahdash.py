def count(n,data):
        oc=0
        ec=0
        for i in range(n):
                if data[i]%2==0:
                        ec+=1
                if data[i]%2:
                        oc+=1
        return ("oc:",oc,"ec:",ec)
n=int(input())
data=list(map(int,input().split()))
count=count(n,data)
'''
num=int(input())
data=list(map(int,input().split()))
ec=0
oc=0
for i in range(num):
        if data[i]%2==0:
                ec+=1
        if data[i]%2:
                oc+=1
print(ec,oc)
 '''
