'''#with fuction 
def harshad_number(num):
    temp=num
    res=0
    while temp:
        r=temp%10
        temp=temp//10
        res=res+r
    if num%res==0:
        q=num//res
        return ('it_is_a_harshad_number',q)
    return 'it_is_not_a_harshad_number'

num=int(input())
print(harshad_number(num))'''
#normal function
num=int(input())
temp=num
res=0
while temp:
    r=temp%10
    temp=temp//10
    res=res+r
print(res)
if num%res==0:
    q=num//res
    print("it is a harshad number",'\n',q)
else:
    print("not a harshad number")
'''
10)91(9
   90
--------
    1
--------
'''
