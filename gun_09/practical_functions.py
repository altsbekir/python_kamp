#örnek:
def divide_number(number):
    return number / 2
my_list = [10, 20, 30, 40, 50, 60]
my_result_list = []
for number in my_list:
    my_result_list.append(divide_number(number))
print(my_result_list)

#map fonksiyonu
print(map(divide_number, my_list))
#my list'in her elemanı için divide number fonksiyonunu çalıştırır
print(list(map(divide_number, my_list)))

#örnek:
def control_string(string):
    return "zehra" in string
print(control_string("bekir"))
print(control_string("zehra"))
#map'le yapalım
my_string_list = ["zehra", "bekir", "zehra'm", "sA", "xd"]
print(list(map(control_string, my_string_list)))

#filter
#map ile benzer çalışır, True/False yazmak yerine elemanları gösterir
print(list(filter(control_string, my_string_list)))

#lambda
multiply_lambda = lambda number: number * 3
print(multiply_lambda(20))
#type'ı fonksiyondur
print(type(multiply_lambda))
#geriye değer döndürür
result = multiply_lambda(10)
print(result)
print(type(result))

#hızlı, pratik ve anonim fonksiyonlar için lambda'yı kullanırız
number_list = [10, 20, 30, 40, 50]
print(list(map(lambda number: number / 4, number_list)))