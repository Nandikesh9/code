def merge(a,b,m,n):
      c=[0]*(m+n)
      #print(*c)
      
      i=0
      j=0
      k=0
      while i<m and j<n:
            if a[i]<=b[j]:
                  c[k]=a[i]
                  i+=1
                  k+=1
            else:
                  c[k]=b[j]
                  j+=1
                  k+=1
      '''            
      while i<m:
            c[k]=a[i]
            i+=1
            k+=1
      while j<n:
            c[k]=b[j]
            j+=1
            k+=1
      '''
      return c
      
m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=merge(a,b,m,n)
print(c)

'''
            
      
'''
