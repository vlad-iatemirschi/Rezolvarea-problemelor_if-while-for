'''Se dau numerele naturale m și n, unde m<n Să se verifice dacă n este o putere a lui m'''
import math
m=int(input("m="))
n=int(input("n="))
if m>n or m==n:
    print("in conditie se cere ca m sa fie < n")
else:
    i=round(math.log(n,m))
    if m**i==n:
        print("n este o putere")
    else:
        print("n nu este o putere")
