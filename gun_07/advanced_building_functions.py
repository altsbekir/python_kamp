#range 0'dan sayıya kadar liste oluşturur
print(range(50))
range_list = list(range(10))
print(range_list)

#alt sınır belirtebiliriz
my_list = list(range(5, 25))
print(my_list)

#artış miktarı da belirleyebiliriz
print(list(range(5, 25, 2)))

#index bulmak
my_list2 = [10, 20, 30, 40, 50]
for x in range(len(my_list2)):
    print(x)

#enumerate
for element in enumerate(my_list2):
    print(element)

for (ix, value) in enumerate(my_list2):
    print(value)

#random
#rastgele sayı getirmek
from random import randint
print(randint(0, 100))

#karıştırmak
from random import shuffle
shuffle(my_list2)
print(my_list2)

#örnek:
my_list3 = [10, 20, 30, 40, 50, 60, 70]
print(my_list3[randint(0, len(my_list3)-1)])

#zip
food_list = ["apple", "banana", "melon"]
calories_list = [100, 150, 200]
day_list = ["monday", "tuesday", "wednesday"]
zipped_list = zip(food_list, calories_list, day_list)

#yukarıdaki şekilde kullandığımızda veri tipi zip olur:
print(type(zipped_list))
print(zipped_list)

#liste yapıyoruz:
zipped_list = list(zipped_list)
print(type(zipped_list))
print(zipped_list)

#list comprehension
new_list = []
my_string = "Metallica"
for element in my_string:
    new_list.append(element)
print(new_list)
#bu kod bloğunun kısa hali:
new_list = [element for element in my_string]
print(new_list)

#örnek:
number_list = [10, 20, 30, 40, 50, 60]
new_number_list = [number/2 for number in number_list]
print(new_number_list)