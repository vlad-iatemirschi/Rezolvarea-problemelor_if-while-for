'''Sa se calcleze 1!+2!+3!+...+n! (n>1)'''
n=eval(input("dati numarul:"))
if n>1:
    a=1
    b=0
    if n>1:
        for i in range(1,n+1):
            a=a*i
            b=b+a

    else :
         print("n<=1")

print("suma este=",b)
