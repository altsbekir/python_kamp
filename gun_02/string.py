print("Zehra")

isim = "zehra"
print(type(isim))

#bazen çift tırnakla bazen tek tırnakla yazabiliyoruz
print('Zehra')

#capitalize ilk harfi buyuk yazar
print(isim.capitalize())

#not: capitalize'dan sonra () koymak fonksiyonu çalıştırmak anlamına gelir
#parantez olmazsa çalışmaz
print(isim.capitalize)

#fonksiyonlar hakkında bilgi almak için help
#help(isim.capitalize)

#count içindeki belli bir harfin sayısını bulur
print(isim.count("e"))

#upper bütün harfleri büyük harf yapar
print(isim.upper())

isim_upper = isim.upper()
print(isim_upper)

#len karakter sayısını hesaplar (boşlukları da sayar)
print(len(isim))