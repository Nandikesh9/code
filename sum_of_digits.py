from math import sqrt
def isprime(n):
    res=0
    if n==0:
        return 0
    if n>1:
        while n:
            r=n%10
            n=n//10
            res=res+r
    return res


def sumofdigits(n,data):
    for i in range(len(data)):
        data [i]=isprime(data[i])
    return data

n=int(input())
data=list(map(int,input().split()))
sumofdigits(n,data)

'''
num=int(input())
print(isprime(num))'''
#   for sum of primes & non primes
#  return sum(prime),sum(nonprime)
'''
practise question
  54  134 171 481 31
  !!non return vallue
  2# 
'''
