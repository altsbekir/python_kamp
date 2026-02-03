#unique elements (tekil elemanlar): her elemandan bir tane olabilir
#unordered (sırasız): index mantığı yok
my_list = [10, 20, 30, 10, 20, 40, 10, 20, 40]
print(my_list)
my_set = set(my_list)
print(my_set)

#set'e eklemek için .add kullanıyoruz
my_set.add(50)
print(my_set)

#zaten olan elemanı eklemez
my_set.add(10)
print(my_set)

#iki set'i birleştirmek
my_set2 = {30, 40, 50, 60, 70}
print(my_set.union(my_set2))
#tekrar eden elemanları 1 kere alır

#iki set'in kesişimini bulmak
print(my_set.intersection(my_set2))

#örnek:
country_list = ["de", "fr", "tr", "fr", "tr", "tr", "nl", "de", "tr"]
#kaç farklı ülkeye satış yapıldığını nasıl buluruz?
print(len(set(country_list)))

#boş set oluşturmak
empty_set = {}
print(type(empty_set))
#böyle yaptığımızda python bunu dictionary olarak algılar
empty_set = set()
print(type(empty_set))
#doğru yöntem bu

#bu yöntemle boş liste de tanımlanabilir
empty_list = list()
empty_list.append(10)
empty_list.append(20)
empty_list.append(30)
print(empty_list)

#boş sözlük de tanımlanabilir
empty_dictionary = dict()
empty_dictionary["a"] = 10
empty_dictionary["b"] = 20
print(empty_dictionary)