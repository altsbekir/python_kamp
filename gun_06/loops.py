#for loop, while loop
my_list = [10, 20, 30, 40, 50, 60, 70]
for number in my_list:
    print(number)
#burada number değişken ismidir, bir anlamı yoktur. yerine x de yazabilirdik

#6'ya tam bölünenleri yazdırmak
for i in my_list:
    if i % 6 == 0:
        print(i)

#for döngüsü stringlerde de kullanılabilir
name = "bekir"
for letter in name:
    print(letter)

#örnek:
my_new_list = [("a", "b"), ("c", "d"), ("e", "f"), ("g", "h")]
for element in my_new_list:
    print(element)

#tuple unpacking
for (x, y) in my_new_list:
    print(x)

my_tuple_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
for (a, b, c) in my_tuple_list:
    print(a)

#dictionary'de for kullanımı
my_dictionary = {"k1": 100, "k2": 200, "k3": 300}
for element in my_dictionary:
    print(element)
#anahtarları yazar

for (key, values) in my_dictionary.items():
    print(values)

for number in my_dictionary.values():
    print(number)

#continue - break - pass
#döngülerden çıkmak için break
for number in my_list:
    print(number)
    if number == 40:
        print("yes")
        break

#continue durdurur, devamını çalıştırmaz ve sonraki numaradan devam ettirir
for number in my_list:
    print(number)
    if number == 40:
        continue
        print("yes")