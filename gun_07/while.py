#while
#koşul sağlandığı sürece döngü çalışır
x = 0
while x < 10:
    print(x)
    x = x + 1

#örnek:
my_list = [10, 20, 30, 40, 50]
while 20 in my_list:
    print("20 in my list")
    my_list.pop()

#değişkenleri metin içinde yazdırmak için formatlı string kullanırız
print(f"My list is {my_list}")

#örnek:
name = "bekir"
print(f"My name is {name}")
print("My name is", name)
#bu da başka bir yöntem

#örnek:
p = 0
while p < 20:
    print(p)
    p += 1