#key-value pairing (anahtar-değer eşleşmesi)
fruit_list = ["banana", "apple"]
calorie_list = [100, 150]
#iki listedeki elemanları eşlemek istediğimizi düşünelim
fitness_list = {"banana":100, "apple": 150}
print(type(fitness_list))

#burada index mantığı yoktur, anahtar-değer eşleşmeleri vardır
#print(fitness_list[0]) dersek error verir

print(fitness_list["banana"])
print(fitness_list["apple"])
#bu şekilde kullanmak daha sağlıklı

#.keys() anahtarları verir
print(fitness_list.keys())

#.values() değerleri verir
print(fitness_list.values())

print(type(fitness_list.values()))
#liste olarak yazmak istiyorsak
print(list(fitness_list.values()))

#bir anahtarın eşleştiği değeri değiştirmek
fitness_list["banana"] = 200
print(fitness_list)

#burada index mantığı olmadığı için anahtar-değer eşleşmesi yapıldığı anda
#yeni eleman eklenebilir
fitness_list["melon"] = 300
print(fitness_list)

#.get ile eleman getirme mantığı
print(fitness_list.get("apple", 0))
#eğer "apple" listede varsa "apple"ın değerini, yoksa 0'ı getirir

#karışık sözlük oluşturmak
my_mixed_dictionary = {"key1":100, "key2":3.14, "key3":[10, 20, 30]}
#mesela 20'yi çekmek istiyoruz
print(my_mixed_dictionary["key3"][1])

#örnek:
last_dictionary = {"k1":10, "k2":[10, 20, 30, 40, 50], "k3":"string", "k4":{"a":100, "b":200}}
#200'ü nasıl alırız?
print(last_dictionary["k4"]["b"])
#40'ı nasıl alırız?
print(last_dictionary["k2"][3])