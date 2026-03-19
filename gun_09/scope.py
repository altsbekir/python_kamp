#scope
x = 20
def multiply(number):
    x = 5
    return number * x
#burada kod, x = 5'miş gibi davranacak
print(multiply(10)) #sonuç: 50
#ama bu işlemden sonra x'i çekmeye çalışırsak x = 20'ymiş gibi davranır
print(x)

#LEGB (Local Enclosing Global Bıilt-In)
#Global
my_string = "zehra"
def my_function():
    my_string = "zehra 2"
    def my_function2():
        my_string = "zehra 3"
        print(my_string)
#burada my string bizim tanımladığımız değerde
print(my_string)
#my function'u çalıştırdığımızda, my function 2 çalışmaz
my_function()
#şöyle düzeltebiliriz:
def my_function():
    #Enclosing
    my_string = "zehra 2"
    print(my_string)
    def my_function2():
        #Local
        my_string = "zehra 3"
        print(my_string)
    my_function2()
my_function()

#örnek (scope):
y = 10
def new_function(y):
    print(y)
    y = 5
    print(y)
    return y
new_function(10)
print(y)
#görüldüğü gibi fonksiyon y'nin değerini değiştirmiyor
#şöyle değiştirebiliriz:
def changeY():
    global y
    y = 5
    print(y)
changeY()
print(y)