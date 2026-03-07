# 1) Aşağıdaki kodun çıktısı ne olacaktır?
x = 5
y = 3
z = 6
print(x>y and z>x)
#çözüm: True

# 2) Aynı değerlerle kod şu şekilde değiştilirse çıktı ne olacaktır?
print(x<y or z>y)
#çözüm: True

# 3) Aşağıdaki kodun çıktısı ne olacaktır?
'''
yas = 20

if yas < 18:
    print("18 yaşından küçüksünüz")
elif yas >= 18 and yas < 30:
    print("18 ile 30 yaş arasında bir gençsiniz")
elif yas >= 30 and yas < 40:
    print("30 ve 40 arasına gelmişsiniz")
else:
    print("40 yaşından daha büyüksünüz")
'''
#çözüm: 18 ile 30 yaş arasında bir gençsiniz
yas = 20

if yas < 18:
    print("18 yaşından küçüksünüz")
elif yas >= 18 and yas < 30:
    print("18 ile 30 yaş arasında bir gençsiniz")
elif yas >= 30 and yas < 40:
    print("30 ve 40 arasına gelmişsiniz")
else:
    print("40 yaşından daha büyüksünüz")

#4) Aşağıdaki sözlükte, değerler içinde c harfinin geçip geçmediğini gösteren bir if koşulu yazınız
my_dictionary = {"k1":10,"k2k":"a","k32":30,"k4":"c"}
#çözüm:
if "c" in list(my_dictionary.values()):
    print("c var")
else:
    print("c yok")

#5) Aşağıdaki sözlükte, anahtarlar içinde a harfinin geçip geçmediğini gösteren bir if koşulu yazınız
my_other_dictionary = {"b":203,"c":"a","a":400,"d":"f"}
#çözüm:
if "a" in list(my_other_dictionary.keys()):
    print("a var")
else:
    print("a yok")

#6) Aşağıdaki listedeki sayılardan sadece çift sayı olanları yazdıran bir kod yazınız.
my_numbers = [1,2,3,4,5,6,19,20,32,21,20,1111,23,24]
#çözüm:
for number in my_numbers:
    if number%2==0:
        print(number)

#7) Aşağıdaki listedeki sayılar bir dairenin yarı çapını vermektedir.
r_list = [3,2,5,8,4,6,9,12]
#Tüm dairelerin çevresini içeren başka yeni bir liste oluşturunuz. (İpucu: 2 * pi * r)  Pi 3.14 alınabilir.
#çözüm:
cevre_list = []
for element in r_list:
    cevre_list.append(2*3.14*element)
print(cevre_list)

#8) Aşağıdaki listede isim - yaş eşleşmelerinin bulunduğu yapılar mevcuttur.
age_name_list = [("Ahmet",30),("Ayse",24),("Mehmet",40),("Fatma",29)]
# Sadece yaşların olduğu yeni ve ayrı bir liste oluşturunuz.
#çözüm:
only_ages = []
for (name, age) in age_name_list:
    only_ages.append(age)
print(only_ages)

#9) Aşağıdaki müzik gruplarından birini rastgele yazdıran bir kod yazınız
metal_list = ["Metallica","Iron Maiden","Dream Theater","Megadeth","AC/DC"]
#çözüm:
from random import randint
print(metal_list[randint(0, len(metal_list)-1)])

#10) Aşağıdaki kodun çıktısı ne olacaktır?
number_list = [5,7,18,21,20,10,405,24]
print([num % 2 == 0 for num in number_list])
#çözüm: [False, False, True, False, True, True, False, True]