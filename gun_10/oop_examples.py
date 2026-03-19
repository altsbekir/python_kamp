#inheritance
class Musician():
    def __init__(self, name):
        self.name = name
        print("Musician class")
    def test(self):
        print("test1")
    def test2(self):
        print("test2")
bekir = Musician("Bekir")
bekir.test()
bekir.test2()
#Musician+ gibi eski class'ın özelliklerini içerip, üzerine başka eklemeler de
#yapan yeni bir class oluşturmak istediğimizde kalıtımdan faydalanırız
class MusicianPlus(Musician):
    def __init__(self, name):
        Musician.__init__(self, name) #üst sınıftan init çağırıyoruz
        print("Musician plus")
    def test3(self):
        print("test3")
zehra = MusicianPlus("Zehra")

#üst sınıftaki fonksiyonu değiştirmek (override)
class MusicianPlus(Musician):
    def __init__(self, name):
        Musician.__init__(self, name)
        print("Musician plus")
    def test3(self):
        print("test3")
    #override
    def test(self):
        print("test1"*3)
zehra = MusicianPlus("Zehra")
zehra.test()

#polymorphism
class Banana():
    def __init__(self, name):
        self.name = name
    def info(self):
        return f"100 calories {self.name}"
class Apple():
    def __init__(self, name):
        self.name = name
    def info(self):
        return f"150 calories {self.name}"
banana = Banana("Banana")
apple = Apple("Apple")
print(banana.info())
print(apple.info())

#polymorphism aslında aynı isme sahip fonksiyonları farklı class'larda kullanabilmemizdir
fruit_list = [apple, banana]
for fruit in fruit_list:
    print(fruit.info())

#encapsulation (hapsetmek)
class Phone():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def info(self):
        print(f"{self.name} price is {self.price}")
iphone = Phone("Iphone 14", 500)
iphone.info()
#bu haliyle price veya name'i değiştirebiliriz
iphone.price = 400
iphone.info()
#değiştirilemez olmasını istersek şöyle yazarız:
class Phone():
    def __init__(self, name, price):
        self.name = name
        self.__price = price
    def info(self):
        print(f"{self.name} price is {self.__price}")
iphone = Phone("Iphone 14", 500)
#değiştirmeyi tekrar deneyelim:
iphone.__price = 400
iphone.info() #değişmeyecek

#eğer yine de değiştirilmesi gerekirse şöyle yazabiliriz:
class Phone():
    def __init__(self, name, price):
        self.name = name
        self.__price = price
    def info(self):
        print(f"{self.name} price is {self.__price}")
    def changePrice(self, price):
        self.__price = price
iphone = Phone("Iphone 14", 500)
iphone.changePrice(300)
iphone.info()

#abstraction (soyutlama)
from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def maxSpeed():
        pass
#my_car = Car() hata verecektir, çünkü soyut bir sınıftan nesne elde edilemez
#class Tesla(Car):
#    pass
#tesla = Tesla() abstract method olarak tanımladığımız maxSpeed'i zorunlu kılar
class Tesla(Car):
    def maxSpeed(self):
        print("200 km")
tesla = Tesla()
tesla.maxSpeed()

#special methods
class Fruit():
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
my_fruit = Fruit("Banana", 150)
print(my_fruit.calories)
print(my_fruit.name)

#__str__ kullanımı
class Fruit():
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
    def __str__(self):
        return f"{self.name}: {self.calories}"
my_fruit = Fruit("Banana", 150)
print(my_fruit) #return satırından gelen string'i yazar

#__len__ kullanımı
class Fruit():
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
    def __str__(self):
        return f"{self.name}: {self.calories}"
    def __len__(self):
        return self.calories
my_fruit = Fruit("Banana", 150)
print(len(my_fruit))