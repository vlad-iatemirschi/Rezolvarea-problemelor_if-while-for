n=int(input("Dati anul"))
if n>=1000 and n<10000:
    if n%12==0:
        print("anul Maimutei")
    if n%12==1:
        print("anul Cocosului")
    if n%12==2:
        print("anul Cainelui")
    if n%12==3:
        print("anul Porcului")
    if n%12==4:
        print("anul Sobolanului")
    if n%12==5:
        print("anul Boului")
    if n%12==6:
        print("anul Tigrului")
    if n%12==7:
        print("anul Iepurelui")
    if n%12==8:
        print("anul Dragonului")
    if n%12==9:
        print("anul Sarpelui")
    if n%12==10:
        print("anul Calului")
    if n%12==11:
        print("anul Oii")
else:
    print("Ati introdus gresit datele")