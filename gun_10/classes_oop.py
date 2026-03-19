#class
class Person():
    name = ""
    age = 0
bekir = Person()
bekir.name = "bekir alataş"
bekir.age = 20
print(bekir)

#sınıfların içinde özel fonksiyonlar vardır, bunlara method denir ve __ ile yazılır
class Person():
    name = ""
    age = 0
    gender = ""
    #method, initializer
    def __init__(self):
        print("init executed")
bekir = Person()
zehra = Person()

#class'ın içindekileri input'la almak
class Person():
    name = ""
    age = 0
    gender = ""
    #method, initializer
    def __init__(self, nameInput, ageInput, genderInput):
        name = nameInput
        age = ageInput
        gender = genderInput
        print("init executed")
bekir = Person("Bekir", 20, "Male")
print(bekir.name) #yazdığımızda hala name hala "" olarak geliyor
#düzeltmek için sınıfın kendisine referans vermemiz gerekir
class Person():
    #property
    name = ""
    age = 0
    gender = ""
    #initializer method
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print("init executed")
bekir = Person("Bekir", 20, "Male")
print(bekir.age)

#python'a özel olarak property'leri her zaman yazmaya gerek yoktur
class Person():
    #property
    #name = ""
    #age = 0
    #gender = ""
    #initializer method
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print("init executed")
bekir = Person("Bekir", 20, "Male")
print(bekir.age)

#self'le ilgili örnek:
class Person():
    #property
    #name = ""
    #age = 0
    #gender = ""
    #initializer method
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print("init executed")
    def print_age(self):
        print(self.age) #self kullanmazsak olmaz
bekir = Person("Bekir", 20, "Male")
bekir.print_age()

#property'de olan bir şeyi değiştirmek
class Person():
    #property
    #name = ""
    #age = 0
    #gender = ""
    job = ""
    #initializer method
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print("init executed")
    def print_age(self):
        print(self.age) 
bekir = Person("Bekir", 20, "Male")
bekir.job = "AI Engineer"
print(bekir.job)

#class örnek:
class Dog():
    def __init__(self, age):
        self.age = age
karabas = Dog(3)
print(karabas.age)

#köpeğin insan yaşını bulan method'u yazalım:
class Dog():
    year = 7 #daha sonra yılı değiştirebilmek için property'de tanımladık
    def __init__(self, age):
        self.age = age
    def humanAge(self):
        return self.age * self.year
karabas = Dog(3)
print(karabas.humanAge())