#tuple'lar dizi gibidir ama içindeki elemanlar değiştirilemez, güncellenemez
#immutability (değiştirilemezlik) özelliği
my_tuple = [10, "a", "b", 3.14]
print(my_tuple)

#tuple'la yapabileceğimiz iki işlem var
#.index() elemanın index'ini bulur
print(my_tuple.index(10))
#.count() elemandan kaç tane olduğunu sayar
print(my_tuple.count(10))