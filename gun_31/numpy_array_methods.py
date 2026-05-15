import numpy as np

# slicing numpy dizisinde de vardır
my_numpy_list = np.arange(0, 20)
print(my_numpy_list[4: 9])
my_numpy_list[4: 9] = -10 # normal python listesi bu komutu desteklemez
print(my_numpy_list) # 4-9. indexler arasını -10 ile doldurur

# numpy dizileri referans vererek çalışır:
other_list = np.arange(0, 15)
slicing_list = other_list[4: 9]
slicing_list[:] = 100 # slicing_list'teki tüm elemanları 100 e eşitledik
print(other_list) # slicing_list'te yaptığımız değişiklik other_list'i doğrudan etkiledi
# bunun sebebi numpy'ın other_list'in adresi üzerinden işlem yapmasıdır

# copy
numpy_list = np.arange(0, 20)
numpy_list_copy = numpy_list.copy()
slicing_list2 = numpy_list_copy[4: 9]
slicing_list2[:] = 100
print(slicing_list2) # değişti
print(numpy_list_copy) # değişti
print(numpy_list) # değişmedi

# numpy operations with numpy arrays
new_array = np.random.randint(0, 150, 25)
print(new_array)
print(new_array > 50) # true - false listesi döndürür
result_array = new_array > 50
print(result_array)
print(new_array[result_array]) # sadece 50'den büyük olan sayılardan oluşan bir dizi

# numpy'da dizi toplamak
last_array = np.arange(0, 20)
print(last_array + last_array) # python listelerinde elemanları üstüne eklerdi, burada gerçekten toplama işlemi yapılır
print(last_array * last_array) # çarpma işlemi
print(last_array - last_array) # elemanları kendisinden çıkarır, 0'lardan oluşan bir dizi döner
print(last_array / last_array) # bölme işlemi, 1'lerden oluşan bir dizi döner, ilk eleman (0/0) nan döner

# max, min ve mean'in farklı bir kullanımı
print(np.max(last_array))
print(np.min(last_array))
print(np.mean(last_array))

# karekök (sqrt)
print(np.sqrt(last_array))