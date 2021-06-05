from math import sqrt
def isprime(n):
    if n==0:
        return 0
    s=int(sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return 0
    return 1

def findprime(n,data):
    prime=[]
    nonprime=[]
    for i in data:
        if isprime(i):
            prime.append(I)
        else:
            nonprime.append(i)

n=int(input())
data=list(map(int,input.split()))
prime=findprime(n,data)
print(*prime)
'''
num=int(input())
print(isprime(num))'''
#   for sum of primes & non primes
#  return sum(prime),sum(nonprime)
