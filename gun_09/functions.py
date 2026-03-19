#functions
#kod bloklarıdır, kodumuzu daha düzgün yazmamıza olanak tanır, girdi-çıktı alabilir

#fonksiyon nasıl yazılır?
def hello_python():
    print("hello")
    print("python")
#kullanımı
hello_python()

#input
def hello_name(name):
    print("hello")
    print(name)
hello_name("bekir")

#örnek:
def sum_example(sum1, sum2):
    print(sum1+sum2)
sum_example(4, 6)

#default değer belirlemek
def hello_surname(surname = "alataş"):
    print("hello")
    print(surname)
#surname'i biz verirsek verdiğimiz değeri, yoksa default değeri yazar
hello_surname()
hello_surname("alataş2")

#return
def summation(num1, num2, num3):
    print(num1 + num2 + num3)
#bu fonksiyonun bir şey döndürmediğini şöyle anlarız:
x = summation(10, 2, 8)
#ekrana 20 yazar ancak;
print(x)
print(type(x))
#none verir. çünkü fonksiyon sadece ekrana çıktı basar, sonuç üretmez

#çözüm:
def return_summation(num1, num2, num3):
    return num1 + num2 + num3
x = return_summation(10, 2, 8)
print(x)

#args (arguments), kwargs(key word arguments)
def args_sum(*args):
    return sum(args)
print(args_sum(10, 20, 30, 40, 50))

def args_print(*args):
    print(args)
args_print(10, 20, 30, 40, 50)

#kwargs
def kwargs_print(**kwargs):
    print(kwargs)
kwargs_print(apple = 100, banana = 150, melon = 200)