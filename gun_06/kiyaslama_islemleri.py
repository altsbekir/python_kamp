#eşitlik kontrolü yapmak
x = 10
y = 8
#x = y -> x'in değerini y'nin değerine eşitler
#eşitmi kontrol etmek için == operatörünü kullanırız
print(x==y)
#!= operatörü eşit değildir demektir
print(x!=y)

#ve bağlacı -> and
print(2>1 and 3>2)
print(2>1 and 3<2)

#ve bağlacının durumları
print(True and False)
print(True and True)
print(False and False)

#veya bağlacı -> or
print(2>1 or 3>2)
print(2<1 or 3<2)

#veya bağlacının durumları
print(True or True)
print(True or False)
print(False or False)

#not durumu tersine çevirir
print(not 1==1)

#liste içinde eleman kontrolü
print(10 in [10,20,30])
print(5 not in [10,20,30])

#in kontrolü set'lerde de geçerli
print(10 in {10,20,30})
#ama dictionary'de geçerli değildir
my_dictionary = {"a": 10, "b": 20, "c": 30}
#10'a veya b'ye bakmak istiyorsak
print(10 in my_dictionary.values())
print("b" in my_dictionary.keys())

#tuple'larda da geçerli