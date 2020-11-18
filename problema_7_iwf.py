'''
Mihai are un unchi bogat care i-a dăruit în ziua când s-a născut un dolar, iar în fiecare an următor el dubla cadoul și mai adăuga atâția 
dolari câți ani implinea Mihai.
a)Să se calculeze câți dolari a pimit Mihai atunci când împlinit n ani (n<20).
b)La ce vârstă cadoul lui Mihai a fost mai mare de 100$?
'''
n=int(input("Introduceti varsta "))
a=1
b=1
for i in range(1,n+1):
    a=a*2+i
print("la varsta de",n,"ani, Mihai a primit",a,"dolari")

c=0
while (b<100):
    c=c+1
    b=b*2+c
print("Cadoul lui Mihai a fost mai mare de 100$ la varsta de",c,"ani")
