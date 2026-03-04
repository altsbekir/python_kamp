#stringlerde de eşitlik kontrolleri vardır
my_superhero = "Batman"
print(my_superhero == "Batman")

#python'da boşluklar çok önemlidir (indentation da denir), kod blokları buna
#göre oluşur

#if kontrolü
if my_superhero == "Batman":
    print("Bekir")
#if bloğu ancak sonuç True olduğunda çalıştırılır

#elif (else if) kontrolü
my_superhero = input("enter superhero: ")
if my_superhero == "superman":
    print("superman")
elif my_superhero == "batman":
    print("batman")
elif my_superhero == "aquaman":
    print("aquaman")
elif my_superhero == "ironman":
    print("ironman")

#hiçbir durum sağlanmazsa?
if my_superhero == "superman":
    print("superman")
elif my_superhero == "batman":
    print("batman")
else:
    print(":(")