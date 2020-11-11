"""se da numarul n ce apartine (28,29,30,31) sa se afiseze lunile cu numarul n de zile"""
n=int(input("dati numarul de zile:"))
if (n==28):
    print("Februarie")
if (n==29):
    print("Februarie, an bisect")
if (n==30):
    print("Aprilie; iunie; septembrie; noiembrie")
if (n==31):
    print("Ianuarie; martie; mai; iulie; august; octombrie; decembrie")
if (n>31)or(n<28):
    print("luna nu are atatea zile")