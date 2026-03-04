#1) Aşağıdaki değişkenin 5. harfini bir değişkene atayınız
my_string = "Python Ogreniyorum"
#çözüm:
x = my_string[4]
print(x)

#2) Asagidaki string'in 5. ve 8. karakteri arasindaki tum harfleri yazdiriniz (5 ve 8 dahil)
my_new_string = "ProglamlamayaMerhabaDedik"
#çözüm:
print(my_new_string[4:8:])

#3) Aşağıdaki string'i kod ile tersten yazın
my_last_string = "Afyonkarahisarlilastiramadiklarimizdanmisiniz"
#çözüm:
print(my_last_string[::-1])

#4) Aşağıdaki işlemin sonucu hangi veri tipinden olacaktır
4 + 12.2 + 48
#çözüm: float
print(type(4+12.2+48))

#5) Aşağıdaki işlemin sonucu kaçtır
5 + 7 * 12
#çözüm: 89
print(5+7*12)

#6) Bu listeyi en az 2 yoldan oluşturunuz: [1, 3, "a"]
#çözüm 1: listeyi doğrudan oluşturmak
my_list = [1, 3, "a"]
print(my_list)
#çözüm 2: değişkenleri ayrı tanımlayıp, listeye atmak
x = 1
y = 3
z = "a"
my_list2 = [x, y, z]
print(my_list)
#çözüm 3: boş liste tanımlayıp append'le içine atmak
empty_list = list()
empty_list.append(1)
empty_list.append(3)
empty_list.append("a")
print(empty_list)

#7) Aşağıdaki "b"yi tek satırda alınız
my_list = [3.14,4,[2,3,"b"],True]
#çözüm:
print(my_list[2][2])

#8) Aşağıdaki "a"yı tek satırda alınız
my_dictionary = {"key1":20.25, "kk2":[40,{"k21":"a"}]}
#çözüm:
print(my_dictionary["kk2"][1]["k21"])

#9) Aşağıdaki liste set'e çevirilince hangi değerler içinde kalacaktır
my_list_to_be_set = [3,4,9,3,21,22,4,3,9,10,21,22]
#çözüm: 3, 4, 9, 21, 22, 10
my_set = set(my_list_to_be_set)
print(my_set)

#10) Aşağıdaki ifadenin sonucu ne olacaktır
x = 30 * 5 + 3
y = 108 - 2 * 4
x > y
#çözüm: x = 153, y = 100. True çıkar
print(x>y)