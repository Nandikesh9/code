'''num=int(input())
s=0
i=0
while num:
   s=num//2
   print(num)
   i=s
   print(i)
   if i*(i*1)==num:
    print("it is a pronic number")
else:
    print("not a pronic number")'''
'''def isarmstrong(num):
    temp=num
    dc=0
    while temp:
        temp=temp//10
        dc+=1
    res=0
    temp=num
    while temp:
        r=temp%10
        temp=temp//10
        res=res+pow(r,dc)
    if num==res:
        return "isarmstrong"
    return "not a armstrong"
num=int(input())
print(isarmstrong(num))'''

def is_a_disarium_number(num):
  temp=num
  res=0
  ic=0
  dc=0
  while temp:
     temp=temp//10
     ic+=1
  while temp:
     r=temp%10
     temp=temp//10
     res=res+pow(r,dc)
     dc-=1
     print(res)
  if res==num:
        return True
  return False
num=int(input())
print(is_a_disarium_number(num))
    
