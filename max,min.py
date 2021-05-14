num=int(input('krama sonkya'))#5096
mi=9
ma=0
while num:
    r=num%10   #  6  9   0   5
    num=num//10#509  50  5   0
    temp=r
    if temp>ma:
        ma=temp
    if temp<mi:
        mi=temp
print(ma,mi)
