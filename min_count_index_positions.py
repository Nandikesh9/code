def s_max_s_min(n,data):
      s,l,c,rev=data[0],data[0],0,0
      for i in data:
            if s<i:
                  s=i
            while s:
                  r=s%10
                  s=s//10
                  c=c*10+r
            if s>i:
                  l=i
            while l:
                  r2=l%10
                  l=l//10
                  rev=rev*10+r2
            if rev<i: 
                  return ("super max:",rev)
n=int(input())
data=list(map(int,input().split()))
maxi=s_max_s_min(n,data)
print(maxi)
