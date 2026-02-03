#string özellikleri tek bir elemanın değiştirilmesini desteklemez
my_string = "zehra"
#my_string[0] = "a" yazarsak error verir
#bu özelliğe immutability (değiştirilemezlik) denir

#liste veri tipi
my_list = [10, 20, 30]
print(type(my_list))
x = 10
y = 20
z = 30
my_list = [x, y, z]
print(my_list)

#index mantığı burada da geçerli
print(my_list[0])

#listelerde index'lerde tutulan değerleri değiştirmek mümkün
my_list[0]=100
print(my_list)

#eleman sayısını bulmak için len kullanabiliriz
print(len(my_list))

#sonuna eklemek için append kullanırız
my_list.append(80)
print(my_list)

#liste içindeki bir elemanın sayısını bulmak için .count kullanırız
print(my_list.count(20))

#bir elemanın kaçıncı indexte olduğunu bulmak için .index kullanırız
print(my_list.index(80))

#.insert(index, object) object'i index numarasına ekler, gerisini sağa kaydırır
my_list.insert(2, 35)
print(my_list)

#.pop son elemanı atar
my_list.pop()
print(my_list)

#.remove() neyi istersek onu çıkartır
my_list.remove(100)
print(my_list)

#.reverse tersine çevirir
my_list.reverse()
print(my_list)

#.sort küçükten büyüğe sıralar
my_list.sort()
print(my_list)

#kullanıcıdan bir x değeri almak
x = input("enter x: ")
print(x)
#inputla alınan değer her zaman string'tir
print(type(x))

#input'larla liste oluşturmak
y = input("enter y: ")
print(y)
z = input("enter z: ")
print(z)
input_list = []
print(len(input_list))
input_list.append(x)
input_list.append(y)
input_list.append(z)
print(input_list)

#bu listenin ilk elemanını 2'yle çarpmaya kalkarsak yan yana yazar
#çünkü input'la girdiğimiz zaman daima string alıyor demiştik
print(input_list[1]*2)

#VERİ TİPİ DÖNÜŞTÜRME

#integer'ı string'e dönüştürmek
my_integer = 50
print(type(str(my_integer)))

#string'i integer'a  ve float'a dönüştürmek
my_string = '50'
print(type(int(my_string)))
print(type(float(my_string)))
#eğer string harf vs. içerirse sayıya dönüşemez

#input'la aldığımız listedeki elemanları şöyle çarpabiliriz:
print(int(input_list[1])*2)

#listeleri de string'e çevirebiliriz
print(type(str(input_list)))

#İLERİ SEVİYE LİSTE İŞLEMLERİ

#listeler farklı veri tiplerini içerebilir
mixed_list = ["bekir", 3.14, 100]
print(type(mixed_list))

#listelerde toplama işlemi birbirine ekler
list1 = [10, 20, 30]
list2 = [40, 50, 60]
print(list1+list2)

#listelerde çarpma işlemi aynı listeyi yanına yazarak ilerler
print(list1*2)

#Nested List (Liste İçinde Liste)
my_nested_list = [10, 20, 3.14, "bekir", [1, 2, 3]]
print(my_nested_list[0])
print(my_nested_list[1])
print(my_nested_list[2])
print(my_nested_list[3])
print(my_nested_list[4])
small_list = my_nested_list[4]
print(type(small_list))

#örnek: küçük listede 2'ye ulaşmak
print(my_nested_list[4][1])

#böyle durumlarda küçük liste, büyük listenin içinde yalnızca tek 1 eleman olur
print(len(my_nested_list))