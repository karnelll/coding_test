h, m = map(int, input().split())
t = int(input())
   
if m + t < 60:
    print(h, m + t)

elif h>23 and  m + t > 60:
    print (h + ((m+t)//60), (m+t) % 60)
else:
    print (((h + ((m+t)//60)) %24 ), (m+t) % 60) 