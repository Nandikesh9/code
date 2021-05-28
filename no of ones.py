def no_of_ones(n):
        dc=0
        if n==0:
            return 0
        while n:
            r=n%10
            n=n//10
            if r==1:
                dc=dc+1
        return dc
n=int(input())
print(no_of_ones(n))
