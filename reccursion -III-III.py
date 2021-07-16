def fun(n):
      if n<=1:
            return n
      
      fun(n-1)
      print(n)
      fun(n-2)
      
n=int(input())
fun(n)

'''
            
      
'''
